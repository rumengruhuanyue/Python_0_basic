# -*-coding:UTF-8-*-

import pymysql


def delete_record():
    conn = pymysql.connect('127.0.0.1', 'root', '123456', 'test', 3306, charset='utf8')
    cur = conn.cursor()
    sql = "delete from employee where age >= %d" % 22

    try:
        cur.execute(sql)
        conn.commit()
        print('delete completed!')
    except Exception as e:
        print(f'delete record failed.Case:{e}')
        # 删除途中遇到错误回滚操作
        conn.rollback()
    finally:
        conn.close()


def main():
    delete_record()


if __name__ == '__main__':
    main()

"""
mysql> select * from employee;
Empty set (0.00 sec)
"""
