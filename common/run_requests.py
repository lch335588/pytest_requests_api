from config.config import *
from base import custom_requests
from data import xlsx_data


def do_requests(data_step: dict, session, sheet_name):
    method = data_step[xls_head["method"]]
    url = data_step[xls_head["url"]]
    added = data_step[xls_head["added"]]
    check_sess = xlsx_data.XlsxData().check_session(sheet_name)
    if method:
        if check_sess == 'yes':
            response = custom_requests.Request().\
                session_request(method=method, url=url, session=session, add_parameter_dict=added)
        else:
            response = custom_requests.Request().\
                http_request(method=method, url=url, add_parameter_dict=added)
        return response
    else:
        return None
