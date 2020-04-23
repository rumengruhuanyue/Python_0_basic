import _thread
"""
    # encoding: utf-8
    # module _thread
    # from (built-in)
    This module provides primitive operations to write multi-threaded programs.
    The 'threading' module provides a more convenient interface.
"""
from time import ctime, sleep


"""
【创建 Thread 的实例，传给它一个函数】
"""
loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at', ctime())
    sleep(nsec)
    print('end loop', nloop, 'at', ctime())
    lock.release()  # 此线程任务完成后，解锁


def main():
    """
        thread模块，多线程管理，手动加锁/解锁
        主要用来了解thread线程锁的机制
    """

    print('Starting at', ctime())

    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()  # 声明线程锁
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))  # 线程开启时，加上线程锁

        """
            start_new_thread(function, args[, kwargs])
             (start_new() is an obsolete synonym)
    
            Start a new thread and return its identifier.  The thread will call the
            function with positional arguments from the tuple args and keyword arguments
            taken from the optional dictionary kwargs.
        """

    for i in nloops:
        # 当开启的线程是被锁住的状态就继续循环，以不让主线程向下执行
        # 手动设置让主线程不往下进行，后续使用threading模块会更加容易控制
        # （后面会用threading来管理线程更加方便）
        while locks[i].locked():
            pass
            # pass占位，并无实际意义。
            # 比如单独定义一个函数，空函数程序会报错，
            # 当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。

    # def test():  # IndentationError: expected an indented block 期待一个代码缩进块，即函数定义必须有函数体

    print('all Done at', ctime())


if __name__ == "__main__":
    main()
