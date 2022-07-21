import requests
from config.config import *
import time
import traceback
import ast


class Request:

    def __init__(self):
        self.logdir = os.path.join(project_dir, "result", "log.txt")

    # 日志
    def print_error_log(self):
        nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
        f = open(self.logdir, 'a')
        print(f'{nowtime}\n',
              file=f)
        traceback.print_exc(file=f)
        f.close()
        print(f'{nowtime}\n')

    def http_request(self, method, url, add_parameter_str=None):
        parameter = {
            "params": None,
            "data": None,
            "headers": None,
            "cookies": None,
            "files": None,
            "auth": None,
            "timeout": None,
            "allow_redirects": True,
            "proxies": None,
            "hooks": None,
            "stream": None,
            "verify": None,
            "cert": None,
            "json": None,
        }
        if add_parameter_str:
            add_parameter_dict = ast.literal_eval(add_parameter_str)
            parameter.update(add_parameter_dict)
        try:
            return requests.request(
                method=method,
                url=url,
                params=parameter['params'],
                data=parameter['data'],
                headers=parameter['headers'],
                cookies=parameter['cookies'],
                files=parameter['files'],
                auth=parameter['auth'],
                timeout=parameter['timeout'],
                allow_redirects=parameter['allow_redirects'],
                proxies=parameter['proxies'],
                hooks=parameter['hooks'],
                stream=parameter['stream'],
                verify=parameter['verify'],
                cert=parameter['cert'],
                json=parameter['json'],)
        except:
            self.print_error_log()
            return '{"result":"error","msg":"Please check the log for detailed errors"}'

    def session_request(self, method, url, session: requests.session(), add_parameter_str=None):
        parameter = {
            "params": None,
            "data": None,
            "headers": None,
            "cookies": None,
            "files": None,
            "auth": None,
            "timeout": None,
            "allow_redirects": True,
            "proxies": None,
            "hooks": None,
            "stream": None,
            "verify": None,
            "cert": None,
            "json": None,
        }
        if add_parameter_str:
            add_parameter_dict = ast.literal_eval(add_parameter_str)
            parameter.update(add_parameter_dict)
        try:
            return session.request(
                method=method,
                url=url,
                params=parameter['params'],
                data=parameter['data'],
                headers=parameter['headers'],
                cookies=parameter['cookies'],
                files=parameter['files'],
                auth=parameter['auth'],
                timeout=parameter['timeout'],
                allow_redirects=parameter['allow_redirects'],
                proxies=parameter['proxies'],
                hooks=parameter['hooks'],
                stream=parameter['stream'],
                verify=parameter['verify'],
                cert=parameter['cert'],
                json=parameter['json'],)
        except:
            self.print_error_log()
            return '{"result":"error","msg":"Please check the log for detailed errors"}'


