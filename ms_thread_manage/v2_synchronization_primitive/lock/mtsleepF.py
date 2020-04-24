from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime


class CleanOutputSet(set):  # 继承set类，重写toString方法——>这样，就会在调用此对象时直接输出设置好的str形式
    def __str__(self):
        """
        # 1. x for x in self  ——
        #           set1 = {1,2,1}
        #              —— >  {1, 2}  # 集合类型无序，元素唯一
        #               type(set1)  ——>  <class 'set'>
        #    self ——> set类型
        #    ——> 结果就是set直接的遍历出来的结果，是一个对象<generator object <genexpr> at 0x0000024C0C320820>
        #       ——> list(x for x in set1)
        #                 ——>  [1, 2]
        #       ——> tuple(x for x in set1)
        #                 ——>  (1, 2)
        # 2. builtins.pyi ——> def join(self, iterable: Iterable[str]) -> str: ...
        # 3. Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        # 【小结-1】.join接受一个可迭代对象（比如：list,tuple,string等以及这里的generator object）
        #         并使用.join点'.'前面的分隔符分隔开各个元素—————>返回一个str
        """
        return ', '.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
"""
# list(loops)   ———— 比如： [2, 2, 4, 3, 3, 4]
# print(list(loops))  # 产生3-6个随机值为2-4间的随机数字

# list(x for x in range(randrange(3, 7)))  ——> [0, 1, 2]
#                 ——>即，randrange(3, 7)生成的随机值为3
#                        然后，遍历range(0, 3),且直接输出，并换成list（参数为可迭代对象）类型——> [0, 1, 2]
#
#                                   class list(object)
#                                        |  list(iterable=(), /)
#
# list(randrange(2, 5) for x in range(3)) ——> [3, 3, 4]  ——> 表示randrange(2, 5) 三次分别产生了3, 3, 4三个随机值
# 【小结-2】y for x in iterable_obj
#           ——> 此类型语句，结果中的元素由y表达式确定，结果个数由len(iterable_obj)确定
"""

"""
i = randrange(3, 7))————产生3-7但不包含7的一个随机数字,比如：i = 6
r = range(i)————range(0, 6),  0-6但不包含6
"""
remaining = CleanOutputSet()  # 使用集合来记录剩下的还在运行的线程

"""
# 【小结-3：链式推导式匹配for循环】
# 前面表达式——确定每个元素值且此表达式结果为一个对象不能多个；
# 后面表达式——确定结果中元素个数或者元素未处理前的基础值
# vec = [2, 4, 6]
# 1.    [3*x for x in vec] ——> [6, 12, 18]    # 遍历原始每个元素*3再重新输出由于加了[]所以输出list类型
# 2.    [3*x for x in vec if x > 3] ——> [12, 18]    # 遍历list，若遍历的元素>3则纳入新的序列中，且需要先*3
# 3.    [3*x for x in vec if x < 2] ——> []      # 遍历list发现并没有<2 的元素，所以输出空list
# 4.    [[x,x**2] for x in vec] ——> [[2, 4], [4, 16], [6, 36]]
#             ——> 从前面表达式[x,x**2]看出结果中的每个元素为list；
#             ——> 每个元素list中由遍历出的原始list元素,处理而来
# 5.    [(x, x**2) for x in vec] ——> [(2, 4), (4, 16), (6, 36)] ——> [(2, 4), (4, 16), (6, 36)]
#             ——> 从前面表达式[x,x**2]看出结果中的每个元素为tuple；与上面 4. 的list案例类似
#             ——> 每个元素tuple中由遍历出的原始list元素,处理而来

# 6     [3*x for x in vec if x > 3] ——> [12, 18]
# 7.    [3*x for x in vec if x > 3] ——> [12, 18]
# -----------------------------------------------------------------------------------------------------------
# vec1 = [2, 4, 6]
# vec2 = [4, 3, -9]
# 8.    [x*y for x in vec1 for y in vec2] ——> [8, 6, -18, 16, 12, -36, 24, 18, -54]
#             ——> for x in vec1 ——为外循环 ； for y in vec2 ——为内循环  ； x*y为每次运算表达式 ；[] 括起来——输出list
# 9.    [x+y for x in vec1 for y in vec2] ——> [6, 5, -7, 8, 7, -5, 10, 9, -3]
#             ——> 类似 8. 只不过运算表达式不同
# 10.   [vec1[i]*vec2[i] for i in range(len(vec1))] ——> [8, 12, -54]
#             ——> 先看运算表达式为对应元素相乘 ； 然后看后面范围为前len(vec1)个元素对应相称  ； [] 输出list
#             ——> 这个地方要注意后面的表达式中是len(vec1)还是len(vec2)，按照前面表达式看，要选择长度短的，以免下标越界
#             vec1 = [1, 2, 3]
#             vec2 = [1, 2, 3, 4]
#             [vec1[i]*vec2[i] for i in range(len(vec1))]  ——> [1, 4, 9]
#
#             ——> 但是下面的会有异常（越界）：
#             [vec1[i]*vec2[i] for i in range(len(vec2))] ——>IndexError: list index out of range
# 11. 加强10. [vec1[i]*vec2[i] for i in range(len(vec1 if len(vec1)<=len(vec2) else vec2))] ——> [1, 4, 9]
"""


def loop(nsec):
    myname = currentThread().name  # type(currentThread().name)  ->   <class 'str'>
    # I/O 和访问相同的数据结构都属于临界区，因此需要用锁来防止多个线程同时进入临界区
    # 这里加锁，以确保线程启动输出的内容，线程间不竞争，避免打印异常，避免输出可能部分混乱
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    # 格式化字符串，%s占位，字符串型
    # print('输出的字符串结构设置好' % 占位参数传入）
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('[%s] Completed %s (%d sdecs)' % (ctime(), myname, nsec))
        print('    (remaining: %s)' % (remaining or 'NONE'))


def _main():
    """
    遍历序列：——>每次返回一个序列中的元素
    for pause in [1,2,5]:
         print(pause,end=" ")

    1 2 5
    """
    for pause in loops:  # list(loops)   ———— 比如： [2, 2, 4, 3, 3, 4]
        Thread(target=loop, args=(pause,)).start()  # 遍历loops，开启len(loops)个线程，每个线程休息时间为loops中各个随机值


@register
def _atexit():
    print("all DONE at:", ctime())


if __name__ == "__main__":
    _main()
    # 偶尔会不正常
    """
    [Fri Apr 24 22:44:21 2020] Started Thread-1
    [Fri Apr 24 22:44:21 2020] Started Thread-2
    [Fri Apr 24 22:44:21 2020] Started Thread-3
    [Fri Apr 24 22:44:21 2020] Started Thread-4
    [Fri Apr 24 22:44:21 2020] Started Thread-5
    [Fri Apr 24 22:44:23 2020] Completed Thread-4 (2 sdecs)
        (remaining: Thread-2, Thread-5, Thread-1, Thread-3)[Fri Apr 24 22:44:23 2020] Completed Thread-3 (2 sdecs)
        (remaining: Thread-2, Thread-5, Thread-1)

    [Fri Apr 24 22:44:23 2020] Completed Thread-5 (2 sdecs)
        (remaining: Thread-2, Thread-1)
    [Fri Apr 24 22:44:24 2020] Completed Thread-1 (3 sdecs)
        (remaining: Thread-2)
    [Fri Apr 24 22:44:25 2020] Completed Thread-2 (4 sdecs)
        (remaining: NONE)
    all DONE at: Fri Apr 24 22:44:25 2020
    """
    # 偶尔也会正常，但是加锁能保证一直正常输出不会乱
    """
    [Fri Apr 24 22:47:34 2020] Started Thread-1
    [Fri Apr 24 22:47:34 2020] Started Thread-2
    [Fri Apr 24 22:47:34 2020] Started Thread-3
    [Fri Apr 24 22:47:34 2020] Started Thread-4
    [Fri Apr 24 22:47:34 2020] Started Thread-5
    [Fri Apr 24 22:47:34 2020] Started Thread-6
    [Fri Apr 24 22:47:36 2020] Completed Thread-1 (2 sdecs)
        (remaining: Thread-4, Thread-5, Thread-6, Thread-3, Thread-2)
    [Fri Apr 24 22:47:36 2020] Completed Thread-5 (2 sdecs)
        (remaining: Thread-4, Thread-6, Thread-3, Thread-2)
    [Fri Apr 24 22:47:37 2020] Completed Thread-6 (3 sdecs)
        (remaining: Thread-4, Thread-3, Thread-2)
    [Fri Apr 24 22:47:38 2020] Completed Thread-4 (4 sdecs)
        (remaining: Thread-3, Thread-2)
    [Fri Apr 24 22:47:38 2020] Completed Thread-3 (4 sdecs)
        (remaining: Thread-2)
    [Fri Apr 24 22:47:38 2020] Completed Thread-2 (4 sdecs)
        (remaining: NONE)
    all DONE at: Fri Apr 24 22:47:38 2020
    """
