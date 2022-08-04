import pytest
import time
from base.custom_requests import Request
from common import assert_requests
from common import run_requests
import requests
from data import xlsx_data
from config.config import *


case_data = xlsx_data.XlsxData().sheet_data()
keys = list(case_data.keys())
print(keys)


if len(keys) >= 1:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI01:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[0]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[0])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf

if len(keys) >= 2:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI02:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[1]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[1])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf

if len(keys) >= 3:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI03:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[2]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[2])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf


if len(keys) >= 4:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI04:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[3]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[3])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf


if len(keys) >= 5:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI05:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[4]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[4])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf


if len(keys) >= 6:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI06:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[5]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[5])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf


if len(keys) >= 7:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI07:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[6]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[6])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf


if len(keys) >= 8:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI08:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[7]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[7])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf


if len(keys) >= 9:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI09:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[8]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[8])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf


if len(keys) >= 10:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI10:
        @pytest.fixture(autouse=True)
        def setting(self):
            self.pass_value = {}
            self.session = requests.Session()

        @pytest.mark.parametrize('api_data', case_data[keys[9]])
        def test_sheet(self, api_data):
            response = run_requests.do_requests(api_data, self.session, keys[9])
            if api_data[xls_head['assert_mode']]:
                result_tf = assert_requests.judge(api_data, response)
                assert result_tf


if __name__ == '__main__':
    pytest.main(["-s", "-v", "-n", "3", "--dist=loadscope", "test_case.py"])

