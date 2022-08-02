# _*_ coding: utf-8 _*_
import pytest
import os
if __name__ == '__main__':
    # pytest.main(["-v", "-n", "2", "--dist=loadscope", "./case/test_case.py", '-q', '--alluredir=./result/xml', '--clean-alluredir'])
    # os.system('allure generate ./result/xml -o ./result/html --clean')
    pytest.main(["-v", "-n", "2", "--dist=loadscope", "./case/test_case.py"])


