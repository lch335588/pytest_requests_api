from config.config import *
from base import custom_requests
from data import xlsx_data


def do_requests(data_step: dict, session=None):
    method = data_step[xls_head["method"]]
    url = data_step[xls_head["url"]]
    added = data_step[xls_head["added"]]
    if method:
        if session:
            response = custom_requests.Request().\
                session_request(method=method, url=url, session=session, add_parameter_dict=added)
        else:
            response = custom_requests.Request().\
                http_request(method=method, url=url, add_parameter_dict=added)
        return response
    else:
        return None
