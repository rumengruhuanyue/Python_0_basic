from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)  # 设置了5个装有糖果的盘子


def refill():
    lock.acquire()  # 获取到锁，执行生产糖果的操作
    print('Refilling candy...', end=' ')
    try:
        candytray.release()
    except ValueError:
        print('full, skipping')
    else:
        print('OK')
    lock.release()  # 释放锁


def buy():
    """
    # 消费或者生产candy时访问同一资源，使用同一把锁。
    # 生产时就不允许消耗，消耗时不允许生产，即一时间只允许生产或消耗
    """

    lock.acquire()  # 获取到锁，执行消费糖果的操作

    print('Buying candy...', end=' ')

    # def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    # 这里的bool值设置，意思是阻塞状态下返回这个值，不阻塞的话正常执行
    if candytray.acquire(False):  # 一旦不能获取到，即当前阻塞，阻塞则返回填写的False，则执行else；获取的到则正常执行
        print('OK')
    else:
        print('empty, skipping')
    lock.release()  # 释放锁


def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))     # 随机每次休息


def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def _main():
    print('starting at:', ctime())
    nloops = randrange(2, 6)
    print('The Candy Machine (full with %d bars)' % MAX)
    # 这里人为设定 消费线程 消费candy的次数 >= 生产线程 生产candy的次数
    Thread(target=consumer, args=(randrange(nloops, nloops + MAX + 2),)).start()  # buyer
    Thread(target=producer, args=(nloops,)).start()


@register
def _atexit():
    print('all done at:', ctime())


if __name__ == '__main__':
    _main()

    """
    starting at: Mon Apr 27 18:08:59 2020
    The Candy Machine (full with 5 bars)
    Buying candy... OK
    Buying candy... OK
    Buying candy... OK
    Buying candy... OK
    Buying candy... OK
    Buying candy... empty, skipping
    Buying candy... empty, skipping
    Refilling candy...
    OK
    Refilling candy...
    OK
    all done at: Mon Apr 27 18:09:14 2020
    """
