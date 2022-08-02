import os

project_dir = os.path.dirname(os.path.dirname(os.path.join(__file__)))
# print(project_dir)
# 需执行文件名
file_name = '接口自动化草稿.xlsx'
# 数据库配置
mysql_config = {"host": "localhost",
                "port": 3306,
                "user": "root",
                "password": "123456",
                "database": "test",
                "charset": "utf8"}
# xlsx首行信息
xls_head = {"name": "编号/名称",
            "method": "请求方式",
            "url": "请求url",
            "headers": "请求头",
            "data": "请求体",
            "added": "额外参数",
            "assert_mode": "断言方式",
            "assert_content": "断言内容",
            "extract": "数据提取",
            "file": "参数化文件"
            }
