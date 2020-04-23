import threading
from time import ctime, sleep

loops = [4, 2]

"""
派生 Thread 的子类，并创建子类的实例 
"""


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    # 重写threading.Thread线程类的run方法
    def run(self):
        self.func(*self.args)
        # *self.args —— 收集参数。
        # 若收集参数后面加参数，则建议加关键字参数，否则也可能会被纳入/被认为是收集参数内容


def loop(nloop, nsec):
    print('start loop', nloop, 'at', ctime())
    sleep(nsec)
    print('end loop', nloop, 'at', ctime())


def main():
    """
        引入高级模块threading，多线程管理
        也建议使用threading模块管理线程
    """
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:  # create all threads
        """
            # MyThread继承threading.Thread类，
            # 创建线程直接调用MyThread()
            # 开启线程时直接执行线程的.start()方法
        """
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:  # start all threads
        threads[i].start()

    for i in nloops:  # wait for completion
        threads[i].join()

    print('all done at:', ctime())


if __name__ == '__main__':
    main()
