def fab(n):
    if n < 1:
        print('输入有误！')
    n1 = 1
    n2 = 1
    n3 = 1
    # n-2 > 0 理解为数轴上距离n1位置的最小距离
    # 大于2执行循环体，否则跳出循环，意味着n1与
    # n2已经最靠近n位置了
    while n - 2 > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3


result = fab(20)
print('总共有%d对小兔崽子诞生！' % result)

# 使用迭代效率较递归做法高
