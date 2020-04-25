## 同步原语

1. 多线程编程中一个非常重要的方面：**_同步_**。多线程代码中，**总会有一些特定的函数或代码块不希望（或不应该）被多个线程同时执行**，通常包括修改数据库、更新文件或其他会产生竞态条件的类似情况.

2. 如果两个线程运行的顺序发生变化，就有可能造成代码的执行轨迹或行为不相同，或者产生不一致的数据。

3. 这就是需要使用同步的情况，确保**在给定的时刻只有一个线程可以通过时，就是使用同步的时候了**

4. **I/O 和访问相同的数据结构**都属于**临界区**，因此需要用锁来**防止多个线程同时进入临界区**

5. 程序员选择适合的**同步原语，或者线程控制机制**来**执行同步**。 Python 支持多种同步类型，可以给你足够多的选择。

6. 【其中两种类型的同步原语】：**锁**是所有机制中最简单、最低级的机制；而**信号量**用于多线程竞争 有限资源的情况。

## 锁示例

1. 加锁，以确保线程启动输出的内容，线程间不竞争，避免打印异常，避免输出可能部分混乱
        
        lock = Lock()
        
        def loop(nsec):
            myname = currentThread().name  # type(currentThread().name)  ->   <class 'str'>
            
            # 1. I/O 和访问相同的数据结构都属于临界区，因此需要用锁来防止多个线程同时进入临界区
            # 1.1 这里访问公共资源向集合中添加元素，以及 I/O 向控制台输出，所以加锁
            lock.acquire()
            remaining.add(myname)
                
            # 格式化字符串，%s占位，字符串型
            # print('输出的字符串结构设置好' % 占位参数传入）
            print('[%s] Started %s' % (ctime(), myname))
            lock.release()    
            
            # 2. 这里，每个线程自己休眠即可，并不竞争，所以不需要加锁
            sleep(nsec)
            
            # 3. 这里要向公共资源集合中移除元素，且向控制台输出，需要加锁
            lock.acquire()
            remaining.remove(myname)
            print('[%s] Completed %s (%d sdecs)' % (ctime(), myname, nsec))
            print('    (remaining: %s)' % (remaining or 'NONE'))        
            lock.release() 
          
2. 使用上下文管理 
    * threading 模块的对象 Lock、RLock、Condition、Semaphore 和 BoundedSemaphore 都包含 上下文管理器，也就是说,它们**都可以使用 with 语句**。当使用 with 时，可以进一步简化                  
            
            def loop(nsec):
                myname = currentThread().name  # type(currentThread().name)  ->   <class 'str'>
                with lock:
                    remaining.add(myname)
                    print('[%s] Started %s' % (ctime(), myname))
                sleep(nsec)
                with lock:
                    remaining.remove(myname)
                    print('[%s] Completed %s (%d sdecs)' % (ctime(), myname, nsec))
                    print('    (remaining: %s)' % (remaining or 'NONE'))
                
3. **链式推导式匹配for循环**          
    * 形式：`表达式1 for x in iterator_obj [可选加判断语句/嵌套内部for循环]`  
    * 表达式1：确定结果中每个元素的运算过程
    * 后面的可迭代对象也可以由表达式来取得，其确定了基础的可迭代对象的元素最原始状态，即未处理前的状态。   
            
            loops = (randrange(2, 5) for x in range(randrange(3, 7)))
    
        此语句，`range(randrange(3, 7))`确定了`range`对象其中的数字3-6，比如range(6)
        
        原始的可迭代对象确定了——`range(6)`，而结果中每个元素由`randrange(2, 5)`确定————
        
        * 这里的示例中**表达式1**中不包含`x`，所以最终的结果中与`x`没毛关系
        
        * 也就是表达式1和后面的可迭代对象有关系的，对可迭代对象按照表达式1运算求得各个元素最终值
        
        * 表达式1和后面的可迭代对象元素没有关系的，后面的表达式仅确定最终结果的元素个数即长度，元素由表达式 1 确定