# -*-coding:UTF-8-*-

import pymysql
import datetime


def insert_record():
    conn = pymysql.connect('127.0.0.1', 'root', '123456', 'test', 3306, charset='utf8')
    cur = conn.cursor()
    sql = "insert into employee (first_name, last_name, age, sex, income)" \
          "values('%s', '%s', %d, '%c', %d)" \
          % ('xiao', 'zhi', 22, '男', 3000)

    try:
        cur.execute(sql)
        # 提交到数据库执行
        conn.commit()
        print('insert success!')
    except Exception as e:
        print(f'insert into MYSQL table failed.Case: {e}')
        # 如果发生错误就回滚
        conn.rollback()
    finally:
        conn.close()


def main():
    insert_record()


if __name__ == '__main__':
    main()

"""
mysql> select * from employee;
+------------+-----------+------+------+--------+---------------------+
| first_name | last_name | age  | sex  | income | create_time         |
+------------+-----------+------+------+--------+---------------------+
| xiao       | zhi       |   22 | 男   |   3000 | 2020-05-28 11:57:45 |
+------------+-----------+------+------+--------+---------------------+
1 row in set (0.00 sec)
"""
