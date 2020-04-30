import threading
from atexit import register
from re import compile
from time import ctime
from urllib.request import urlopen
from urllib import request
from concurrent.futures import ThreadPoolExecutor

"""
concurrent.futures模块
传递给 concurrent.futures.ThreadPoolExecutor 的参数是线程池的大小，
在这个应用里就是指要查阅排名的 3 本书。
当然，这是个 I/O 密集型应用，因此多线程更有用。
而对于计算密集型应用而言，可以使用 concurrent.futures.ProcessPoolExecutor 来代替。 
"""
# #1,230,741 in Books
# 匹配'#'+【数字+','至少一次】+' '+'in Books'
REGEX = compile(r"#([\d,]+) in Books ")

AMZN = "http://amazon.com/dp/"

headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 "
           "Safari/537.36")

ISBNs = {
    '0132269937': "Core Python Programming",
    '0132356139': "Python Web Development with Django",
    '0137143419': "Python Fundamentals"
}


def get_ranking(isbn):
    # 使用build_opener()修改报头
    opener = request.build_opener()
    opener.addheaders = [headers]
    url = '{}{}'.format(AMZN, isbn)
    page = opener.open(url)
    data = page.read().decode()
    return REGEX.findall(data)[0]


def _show_ranking(isbn):
    print("- %r ranked %s" % (ISBNs[isbn], get_ranking(isbn)))


def _main():
    print("At", ctime(), "on Amazon...")
    with ThreadPoolExecutor(3) as executor:
        for isbn in ISBNs:
            executor.submit(_show_ranking, isbn)


@register
def _atexit():
    print('all done at:', ctime())


if __name__ == "__main__":
    _main()
