import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', db='scraping')
cur = conn.cursor()
cur.execute("INSERT INTO urls (url, content) values ('www.baidu.com', 'This is content')")
cur.close()
conn.commit()
conn.close()



