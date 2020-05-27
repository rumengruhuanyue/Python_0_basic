import requests
import MySQLdb
from bs4 import BeautifulSoup

conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', db='scraping', charset='utf8')
cur = conn.cursor()

link = "http://santostang.com"
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36'}

r = requests.get(link, headers=heads)

soup = BeautifulSoup(r.text, 'lxml')
title_list = soup.find_all('h1', class_='post-title')
for each in title_list:
    url = each.a['href']
    title = each.a.text.strip()

    cur.execute('insert into urls (url, content) values (%s,%s)', (url, title))

cur.close()
conn.commit()
conn.close()
