# -*-coding:UTF-8-*-

import pymysql


def query_data():
    conn = pymysql.connect('127.0.0.1', 'root', '123456', 'test', 3306, charset='utf8')
    cur = conn.cursor()

    sql = "select * from employee where income > %d" % 1000

    try:
        cur.execute(sql)
        rs = cur.fetchall()  # type(rs)->tuple
        # (
        #       ('xiao', 'zhi', 22, '男', 3000.0, datetime.datetime(2020, 5, 28, 15, 10, 47)),
        #       ('xiao', 'zhi', 22, '男', 3000.0, datetime.datetime(2020, 5, 28, 15, 13, 5))
        # )
        for row in rs:
            first_name = row[0]
            last_name = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            create_time = row[5]
            print(
                f'first_name:\n{first_name}\nlast_name:\n{last_name}\nage:\n{age}\nsex:\n{sex}\nincome:\n{income}'
                f'\ncreate_time:\n{create_time}\n')
            print('-----------------------')
    except Exception as e:
        print(f'Error: unable to fetch data,Error info:{e}')
    finally:
        conn.close()


def main():
    query_data()


if __name__ == '__main__':
    main()
