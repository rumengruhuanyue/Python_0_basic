import threading
from atexit import register
from re import compile
from time import ctime
from urllib.request import urlopen
from urllib import request

"""
由于这是一个 I/O 密集型应用，因此这个程序使用多线程是一个好的选择

由于 Python 虚拟机是单线程（GIL）的原因，只有线程在执行 I/O 密集 
型的应用时才能更好地发挥 Python 的并发性（对比计算密集型应用，它只需要做轮询）

#### 亚马逊图书排名实例
"""


# #1,230,741 in Books
# 匹配'#'+【数字+','至少一次】+' '+'in Books'
REGEX = compile(r"#([\d,]+) in Books ")

AMZN = "http://amazon.com/dp/"

headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 "
           "Safari/537.36")
# 在浏览器中，正常按照url请求，然后进入dev工具查看请求头中User-Agent，在模拟浏览器请求时，加入请求头请求

ISBNs = {
    '0132269937': "Core Python Programming",
    '0132356139': "Python Web Development with Django",
    '0137143419': "Python Fundamentals"
}


def get_ranking(isbn):
    # page = urlopen('{}{}'.format(AMZN, isbn))  # or "%s%s" % (AMZN, isbn)
    # # page = urlopen("%s%s" % (AMZN, isbn))
    # data = page.read().decode()
    # page.close()
    # return REGEX.findall(data)[0]

    # 以上直接请求拼接的url，可以获取到第一本书的排名
    # 但是，第二本就直接抛出503错误

    """
    通过Python爬虫尝试爬去某知名网站的某商品信息，但是在直接调用后却发现
    返回值为503（不是200，表示出错），这种出错的可能有多种，

    因为该网页的来源审查机制限定了HTTP请求的来源——通过什么进行判断是否限制呢？
    通过HTTP header字段进行来源审查的（在HTTP请求头，Python爬虫的User-agent字段会诚实的显示其身份）

    # 怎么办呢？要能修改HTTP请求头自就好了——requests库刚好就提供了这个功能：

    只要在传入headers字段就可以了
    """
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
    for isbn in ISBNs:
        # 1. 单线程
        # _show_ranking(isbn)
        # 2. 多线程
        t = threading.Thread(target=_show_ranking, args=(isbn,))
        t.start()

# 使用 atexit.register()来注册一个退出函数
@register
def _atexit():
    """
    两个地方可以放置 print 语句：_main()返回之后（脚本最后一行）， 或者使用 atexit.register()来注册一个退出函数
    :return:
    """
    print('all done at:', ctime())


if __name__ == "__main__":
    _main()

    """
    # 1. 单线程——20s
    result:
    At Fri Apr 24 18:48:47 2020 on Amazon...
    - 'Core Python Programming' ranked 1,230,741
    - 'Python Web Development with Django' ranked 2,045,791
    - 'Python Fundamentals' ranked 5,789,837
    all done at: Fri Apr 24 18:49:07 2020
    """

    # -----由于这是一个 I/O 密集型应用，因此这个程序使用多线程是一个好的选择------

    """
    # 2. 多线程——9s
    result:
    At Fri Apr 24 19:00:39 2020 on Amazon...
    - 'Python Fundamentals' ranked 5,789,837
    - 'Python Web Development with Django' ranked 2,045,791
    - 'Core Python Programming' ranked 1,230,741
    all done at: Fri Apr 24 19:00:48 2020
    """

    """
    # 3. 当然这个请求跟网络状态有关，访问亚马逊网站，外国网站
    """
