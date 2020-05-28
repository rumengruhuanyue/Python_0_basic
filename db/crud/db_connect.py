# -*-coding:UTF-8-*-
import pymysql


def db_connect():
    # 打开数据库
    db = pymysql.connect('127.0.0.1', 'root', '123456', 'test', 3306, charset='utf8')
    # 创建游标
    cursor = db.cursor()
    # 执行SQL语句
    cursor.execute("SELECT VERSION()")
    # 使用fetchone() 获取单条数据
    data = cursor.fetchone()

    print(f"Database version : {data[0]}")

    # 关闭数据库连接
    db.close()


def main():
    db_connect()


if __name__ == "__main__":
    main()

"""
sudo+ssh://root@192.168.232.128:22/root/anaconda3/envs/py38/bin/python -u /root/tmp/python_o_basic/db/crud/db_connect.py
Database version : 5.7.30
"""