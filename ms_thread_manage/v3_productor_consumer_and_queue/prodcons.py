from random import randint
from time import sleep
from queue import Queue
from ms_thread_manage.moulde_abstract.mythread import MyThread

"""
该生产者-消费者问题的实现使用了 Queue 对象，
以及随机生产（消费）的商品的数量。
生产者和消费者独立且并发地执行线程。 
"""


# writeQ()和 readQ()函数分别用于将一个对象（例如，我们这里使用的字符串’xxx’）放入
# 队列中和消费队列中的一个对象。
# 注意，我们每次只会生产或读取一个对象。
def writeQ(queue):
    print('producing object for Q...', end=' ')
    queue.put('xxx', 1)  # Put an item into the queue.
    print('size now:', queue.qsize())


def readQ(queue):
    val = queue.get(1)  # Remove and return an item from the queue.
    print('consumed object from Q...size now:', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)  # 写入队列数据
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)  # 消耗队列
        sleep(randint(2, 5))


funcs = [reader, writer]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)  # random.randint()与random.randrange()类似，不过它会包括其上限值
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')


if __name__ == "__main__":
    main()
