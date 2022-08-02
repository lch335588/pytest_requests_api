import pymysql
from config.config import *
import time
import traceback


class MysqlJude:
    # 初始化
    def __init__(self, mysql_con=mysql_config):
        self.db = pymysql.connect(host=mysql_con['host'],
                                  port=mysql_con['port'],
                                  user=mysql_con['user'],
                                  password=mysql_con['password'],
                                  database=mysql_con['database'],
                                  charset=mysql_con['charset'],
                                  cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()
        self.logdir = os.path.join(project_dir, "result", "log.txt")

    def close_mysql(self):
        self.cur.close()
        self.db.close()

    def select_mysql(self, sql):
        affected_rows = self.cur.execute(sql)
        actual = self.cur.fetchall()
        print("数据库查询结果:")
        print(actual)
        return actual

    def mysql_log(self):
        nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
        f = open(self.logdir, 'a')
        print(f'{nowtime}\n数据库模块错误！', file=f)
        traceback.print_exc(file=f)
        f.close()
        traceback.print_exc()

    def check_select(self, expect):
        check_res = []
        actual = self.select_mysql(expect['sql'])
        self.close_mysql()
        expect_data = expect['expect']
        if expect['type'] == 'single':
            actual = actual[0]
            for key in expect_data.keys():
                try:
                    if actual[key] == expect_data[key]:
                        check_res.append(True)
                    else:
                        check_res.append(False)
                        print(f"数据库{key}:{str(actual[key])}   预期{key}:{str(expect_data[key])}")
                except:
                    self.mysql_log()
        elif expect['type'] == 'multiple':
            for key in expect_data.keys():
                actual_field_list = []
                for actual_dict in actual:
                    try:
                        actual_field_list.append(actual_dict[key])
                    except:
                        self.mysql_log()
                field_different = set(actual_field_list).difference(expect_data[key])
                field_different.update(set(expect_data[key]).difference(actual_field_list))
                if field_different:
                    check_res.append(False)
                    print(f"{key} 差异:{field_different}")
                else:
                    check_res.append(True)

                # print(actual_field_list)
        # print(check_res)
        return check_res


if __name__ == '__main__':
    my = MysqlJude()




