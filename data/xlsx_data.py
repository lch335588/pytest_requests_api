import ast
import openpyxl
from config.config import *


class XlsxData:
    def __init__(self):
        self.wb = openpyxl.load_workbook(os.path.join(project_dir, "data", file_name))

    def sheet_name_list(self):
        sheetnames_list = self.wb.sheetnames
        for name in sheetnames_list:
            if "test" not in name:
                sheetnames_list.remove(name)
        return sheetnames_list

    def sheet_data(self):
        sheetnames_list = self.sheet_name_list()
        cases_data = {}
        for sheet_name in sheetnames_list:
            ws = self.wb[sheet_name]
            values = list(ws.values)
            if values:
                file = values[0]
                cases_step = []
                for value in values[1:]:
                    case_dict = dict(zip(file, value))
                    case_dict[xls_head['added']] = add_parameter_data(case_dict)
                    case_list = parametric_case(case_dict)
                    cases_step = cases_step + case_list
                cases_data[sheet_name] = cases_step
        return cases_data


def add_parameter_data(step_data):
    add_parameter_dict = {}
    if step_data[xls_head['added']]:
        add_parameter_dict = ast.literal_eval(step_data[xls_head['added']])
    if step_data[xls_head['headers']]:
        headers = {"headers": ast.literal_eval(step_data[xls_head['headers']])}
        add_parameter_dict.update(headers)
    # 请求体默认data传输（后续看是否需要通过headers识别）
    if step_data[xls_head['data']]:
        data = {"data": step_data[xls_head['data']]}
        add_parameter_dict.update(data)
    return add_parameter_dict


def parametric_case(case_dict):
    parametric_file_name = case_dict[xls_head['file']]
    if parametric_file_name:
        case_parametric_list = []
        parametric_data = []
        # 打开读取参数化内文件
        keys_file = open(os.path.join(project_dir, "data", parametric_file_name))
        keys = keys_file.read().splitlines()
        # keys = re.findall('(.*,.*)', keys)
        # print(keys)
        parametric_head = tuple(keys[0].split(','))
        # print(parametric_head)
        # # 参数化文件数据生成[{},{}……]格式数据
        for i in keys[1:]:
            value = tuple(i.split(','))
            # print(value)
            parametric_data.append(dict(zip(parametric_head, value)))

        n_step = 0
        for parametric_dict in parametric_data:
            case_str = str(case_dict)
            for key in parametric_dict.keys():
                case_str = case_str.replace("${" + key + "}", parametric_dict[key])
            case_transition_dict = ast.literal_eval(case_str)
            case_transition_dict[xls_head['name']] = case_transition_dict[xls_head['name']] + '__parametric_' + str(n_step)
            n_step += 1
            case_parametric_list.append(case_transition_dict)

        # print(parametric_data)
        return case_parametric_list
    else:
        return [case_dict]


if __name__ == '__main__':

    XlsxData().sheet_data()