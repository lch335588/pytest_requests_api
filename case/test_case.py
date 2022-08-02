import pytest
import time
from base.custom_requests import Request
from common import assert_requests
from data import xlsx_data


case_data = xlsx_data.XlsxData().sheet_data()
keys = list(case_data.keys())
print(keys)


if len(keys)>=1:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI01:
        def setting(self):
            self.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[0]])
        def test_1(self, api_data):
            print(api_data['编号/名称'])

if len(keys)>=1:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI02:
        def setting(self):
            self.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[1]])
        def test_1(self, api_data):
            print(api_data['编号/名称'])


if __name__ == '__main__':
    pytest.main(["-s", "-v", "-n", "3", "--dist=loadscope", "test_case.py"])

