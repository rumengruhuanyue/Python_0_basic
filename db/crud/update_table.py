# -*-coding:UTF-8-*-

import pymysql


def update_table():
    conn = pymysql.connect('127.0.0.1', 'root', '123456', 'test', 3306, charset='utf8')
    cur = conn.cursor()

    sql = "update employee set age = age + 1 where  sex = '%s'" % '男'

    try:
        cur.execute(sql)
        conn.commit()
        print('update success!')
    except Exception as e:
        print(f'update MYSQL table failed.Case:{e}')
        # 发生错误时回滚
        conn.rollback()
    finally:
        conn.close()


def main():
    update_table()


if __name__ == '__main__':
    main()
