import threading
from time import ctime, sleep

"""
创建 Thread 的实例，传给它一个可调用的类实例 
"""

loops = [4, 2]


class ThreadFunc(object):
    """
        1.在创建线程时，与传入函数相似的一个方法是传入一个可调用的类的实例，
        用于线程执行——这种方法更加接近面向对象的多线程编程。
        这种可调用的类包含一个执行环境，比起一个函数或者从一组函数中选择而言，有更好的灵活性。
        现在有了一个类对象，而不仅仅是单个函数或者一个函数列表/元组。

        2.我们希望这个类更加通用，而不是局限于 loop()函数，因此添加了一些新的东西，
        比如让这个类保存了函数的参数、函数自身以及函数名的字符串。
        而构造函数__init__()用于设定上述 这些值。

        3.当创建新线程时，Thread 类的代码将调用 ThreadFunc 对象，此时会调用__call__()这个特殊方法。
        由于我们已经有了要用到的参数，这里就不需要再将其传递给 Thread()的构造函数了，直接调用即可
    """

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    # 这个类在线程开启后，调用传入的func函数（通过__call__回调），而此函数作为类实例的一个属性存在；

    # 这个类更加通用，而不是局限于 loop()函数，因此添加了一些新的东西，
    # 比如让
    # 这个类保存了函数的参数、函数自身以及函数名的字符串。
    # 而构造函数__init__()用于设定上述 这些值。
    # 当创建新线程时，Thread 类的代码将调用 ThreadFunc 对象，此时会调用__call__()这个 特殊方法

    # 回调函数————类的实例也可以也可以像函数那样调用，执行回调函数中的操作
    def __call__(self):
        # apply(self.func, self.args)   python2 中
        self.func(*self.args)

        # def __call__(self):
        #     # apply(self.func, self.args)   python2 中
        #     self.func(*self.args)


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
        # 创建了threads数组，创建线程t,使用threading.Thread()方法：
        # 在这个方法中,target指向ThreadFunc对象，即它的一个实例，
        # 当创建新线程时，Thread 类的代码将调用 ThreadFunc 对象，此时会调用__call__()这个 特殊方法
        # 把创建好的线程t装到threads数组中。
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        """
            target: Optional[Callable[..., Any]] = ...,
      
            # *target* is the callable object to be invoked by the run()
            # method. Defaults to None, meaning nothing is called.
        """
        # ## 当使用threading.Thread创建线程
        # ## target指向的类的对象，在线程启动，会执行对象的回调函数————实例可以象函数那样执行

        # 如这里的ThreadFunc不可回调，则会报错：
        # TypeError: 'MyThread' object is not callable

        threads.append(t)

    for i in nloops:  # start all threads
        threads[i].start()

    for i in nloops:  # wait for completion
        threads[i].join()
        """
            # 1.join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
            
            # 2.相比于管理一组锁（分配、获取、释放、检查锁状态等）而言，这里只 需要为每个线程调用 join()方法即可。
            
            # 3.join()方法将等待线程结束，或者在提供了超时时间的 情况下，达到超时时间。
            
            # 4.使用 join()方法要比等待锁释放的无限循环（上个例子LockTest.py中使用基础的线程模块thread）
            #   更加清晰（这也是这种锁 又称为自旋锁的原因）。
        """

    print('all done at:', ctime())


if __name__ == '__main__':
    main()
