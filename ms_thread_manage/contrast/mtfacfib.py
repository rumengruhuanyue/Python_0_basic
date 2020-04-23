from ms_thread_manage.moulde_abstract.mythread import MyThread
from time import sleep, ctime


def fib(x):
    """
    斐波那契数列  1, 1, 2, 3, 4, 5 ,...
    加sleep()原因是：计算过快看不出差异
    :param x: 打算计算第几个数列数
    :return: 斐波那契数列数
    """
    sleep(0.005)
    if x <= 2:
        return 1
    return fib(x - 2) + fib(x - 1)


def fac(x):
    """
    阶乘计算  5 * 4 * 3 * ...
    加sleep()原因是：计算过快看不出差异
    :param x: 算谁的阶乘
    :return: 阶乘计算结果
    """
    sleep(0.1)
    if x < 2:
        return 1
    return x * fac(x - 1)


def sum(x):
    """
    累加计算： 5  + 4 + 3 + ...
    加sleep()原因是：计算过快看不出差异
    :param x: 算谁的累加结果
    :return: 累加结果
    """
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum(x - 1)


funcs = [fib, fac, sum]  # 函数名list，可通过函数名调用
n = 12


def main():
    nfuncs = range(len(funcs))
    print('*** SINGLE THREAD')
    for i in nfuncs:
        print('starting', funcs[i].__name__, 'at', ctime())
        print(funcs[i](n))
        print('end', funcs[i].__name__, 'at', ctime())

    print('*** MULTIPLE THREADS')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].get_result())

    print('all done!')


if __name__ == "__main__":
    main()
