import pytest
import time
from base.custom_requests import Request
from common import assert_requests


@pytest.mark.flaky(reruns=1, reruns_delay=2)
class TestCSD:

    @pytest.fixture(autouse=True)
    def setting(self):
        self.pass_value = {}

    # @pytest.mark.parametrize('button_key', keys)
    def test_step(self):
        response = Request().http_request('get', 'http://www.baidu.com')
        # response.encoding = 'utf-8'
        print(response.status_code)
        print(type(response.status_code))
        assert_requests.judge(response)


if __name__ == '__main__':

    pytest.main(["-s", "test_case.py"])

