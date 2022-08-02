import requests
import jsonpath
import ast
import re
from common.check_mysql import MysqlJude
from config.config import *
import time
import traceback


# 日志
def print_error_log():
    logdir = os.path.join(project_dir, "result", "log.txt")
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
    f = open(logdir, 'a')
    print(f'{nowtime}\n断言模块错误！',
          file=f)
    traceback.print_exc(file=f)
    f.close()
    traceback.print_exc()
    print(f'{nowtime}\n断言错误，详情请查看日志')


def judge(case_data: dict, response: requests.Response = None):
    assert_content = ast.literal_eval(case_data[xls_head['assert_content']])
    if response:
        if type(response) is str:
            print(response)
            return False
        elif response.status_code >= 400:
            print(f"状态码:{response.status_code}")
            return False
    try:
        if case_data[xls_head['assert_mode']] == 'jsonpath':
            return check_jsonpath(response, assert_content)
        elif case_data[xls_head['assert_mode']] == 're':
            return check_re(response, assert_content)
        elif case_data[xls_head['assert_mode']] == 'mysql':
            return run_check_mysql(assert_content)
        else:
            print("NO Type!")
            return False
    except:
        print_error_log()
        return False


def check_jsonpath(response: requests.Response, expect_list):
    response_dict = response.json()
    check_res = []
    for expect in expect_list:
        actual = jsonpath.jsonpath(response_dict, expect['expr'])
        if isinstance(actual, list):
            actual = actual[0]
        if expect['type'] == 'eq':
            check_res.append(actual == expect['expected'])

    if check_res:
        return all(check_res)
    else:
        print("断言结果为空，请检查断言内容")
        return False


def check_re(response: requests.Response, expect_list):
    response_str = response.text
    check_res = []
    for expect in expect_list:
        actual = re.findall(expect['expr'], response_str)
        if isinstance(actual, list):
            actual = actual[0]
        if expect['type'] == 'eq':
            check_res.append(actual == expect['expected'])

    if check_res:
        return all(check_res)
    else:
        print("断言结果为空，请检查断言内容")
        return False


def run_check_mysql(mysql_data_dict):
    TF = []
    if mysql_data_dict['config']:
        judge_sql = MysqlJude(mysql_data_dict['config'])
    else:
        judge_sql = MysqlJude()
    result_mysql = judge_sql.check_select(mysql_data_dict)
    TF = TF + result_mysql
    if TF:
        return all(TF)
    else:
        print("断言结果为空，请检查sql")
        return False


if __name__ == '__main__':
    a = {'编号/名称': None, '请求方式': None, '请求url': None, '请求头': None, '请求体': None, '额外参数': {}, '断言方式': 'jsonpath', '断言内容': '[{"expr":"","expected":"","type":"eq"}]', '数据提取': None, '参数化文件': None}
    judge(a)

