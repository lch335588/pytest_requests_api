import requests
import jsonpath
import ast
import re
from common.check_mysql import MysqlJude


def judge(response: requests.Response, expect_raw):
    expect_dict = ast.literal_eval(expect_raw)
    if type(response) is str:
        print(response)
        return False
    elif response.status_code >= 400:
        print(f"状态码:{response.status_code}")
        return False
    else:
        if expect_dict['type'] == 'jsonpath':
            return check_jsonpath(response, expect_dict['content'])
        elif expect_dict['type'] == 're':
            return check_re(response, expect_dict['content'])
        elif expect_dict['type'] == 'mysql':
            return run_check_mysql(expect_dict['content'])
        else:
            print("NO Type!")
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
        return False


def run_check_mysql(mysql_data_list):
    TF = []
    for mysql_data_dict in mysql_data_list:
        if mysql_data_dict['config']:
            judge_sql = MysqlJude(mysql_data_dict['config'])
        else:
            judge_sql = MysqlJude()
        result_mysql = judge_sql.check_select(mysql_data_dict)
        TF = TF + result_mysql
    if TF:
        return all(TF)
    else:
        print("TF为空，请检查sql")
        return False



