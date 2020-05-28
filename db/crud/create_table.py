# -*-coding:UTF-8-*-

import pymysql


def create_table():
    conn = pymysql.connect('127.0.0.1', 'root', '123456', 'test', 3306, charset='utf8')
    cur = conn.cursor()

    cur.execute('drop table if exists  employee')

    sql = """create table employee (
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float,
        create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"""

    try:
        cur.execute(sql)
        print('create table success.')
    except Exception as e:
        print(f'create table failed, case:{e}')
    finally:
        conn.close()


def main():
    create_table()


if __name__ == '__main__':
    main()


"""
远程主机mysql命令行，查看创建的表的结构：
————————————————————————————————————————
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| scraping           |
| sys                |
| test               |
+--------------------+
6 rows in set (0.00 sec)

mysql> use test;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

mysql> desc test
    -> ;
ERROR 1146 (42S02): Table 'test.test' doesn't exist

mysql> desc employee; 
+-------------+-----------+------+-----+-------------------+-------+
| Field       | Type      | Null | Key | Default           | Extra |
+-------------+-----------+------+-----+-------------------+-------+
| first_name  | char(20)  | NO   |     | NULL              |       |
| last_name   | char(20)  | YES  |     | NULL              |       |
| age         | int(11)   | YES  |     | NULL              |       |
| sex         | char(1)   | YES  |     | NULL              |       |
| income      | float     | YES  |     | NULL              |       |
| create_time | timestamp | NO   |     | CURRENT_TIMESTAMP |       |
+-------------+-----------+------+-----+-------------------+-------+
6 rows in set (0.00 sec)

"""
