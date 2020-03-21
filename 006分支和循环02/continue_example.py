for i in range(10):
    if i % 2 != 0:   # 判断被2整除余数不是0，即不是偶数时
        print(i)
        continue    # 结束当前循环，判断循环条件是否满足，满足的话开启下一轮循环
    i += 2
    print(i)
        
