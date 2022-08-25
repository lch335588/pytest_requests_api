import pytest
import time
from common import assert_requests
from common import run_requests
import requests
from data import xlsx_data
from config.config import *


case_data = xlsx_data.XlsxData().sheet_data()
keys = list(case_data.keys())
keys_length = len(keys)
print(keys)


def get_extract(api_data, key, session, pass_value):
    if api_data[xls_head['extract']]:
        extract_response = run_requests.do_requests(api_data, session, key)
        extract_values = xlsx_data.pick_up_value(api_data[xls_head['extract']], extract_response)
        pass_value.update(extract_values)
    return pass_value


def business_order(api_data, key, session, pass_value):
    api_data = xlsx_data.update_data(api_data, pass_value)
    response = run_requests.do_requests(api_data, session, key)
    assert_requests.base_judge(response)
    if api_data[xls_head['assert_mode']]:
        result_tf = assert_requests.judge(api_data, response)
        assert result_tf


if keys_length > 0:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI00:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[0]])
        def test_sheet(self, api_data):
            key = keys[0]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)

if keys_length > 1:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI01:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[1]])
        def test_sheet(self, api_data):
            key = keys[1]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)

if keys_length > 2:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI02:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[2]])
        def test_sheet(self, api_data):
            key = keys[2]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)

if keys_length > 3:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI03:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[3]])
        def test_sheet(self, api_data):
            key = keys[3]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)


if keys_length > 4:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI04:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[4]])
        def test_sheet(self, api_data):
            key = keys[4]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)


if keys_length > 5:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI05:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[5]])
        def test_sheet(self, api_data):
            key = keys[5]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)


if keys_length > 6:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI06:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[6]])
        def test_sheet(self, api_data):
            key = keys[6]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)


if keys_length > 7:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI07:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[7]])
        def test_sheet(self, api_data):
            key = keys[7]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)


if keys_length > 8:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI08:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[8]])
        def test_sheet(self, api_data):
            key = keys[8]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)


if keys_length > 9:
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    class TestAPI09:
        @classmethod
        def setup_class(cls):
            cls.session = requests.Session()
            cls.pass_value = {}

        @pytest.mark.parametrize('api_data', case_data[keys[9]])
        def test_sheet(self, api_data):
            key = keys[9]
            self.pass_value = get_extract(api_data, key, self.session, self.pass_value)
            business_order(api_data, key, self.session, self.pass_value)


if __name__ == '__main__':
    pytest.main(["-s", "-v", "-n", "3", "--dist=loadscope", "test_case.py"])

