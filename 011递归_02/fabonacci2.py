def fab(n):
    if n < 1:
        print('输入有误！')
        return -1

    if n == 1 or n == 2:
        return 1
    return fab(n - 1) + fab(n - 2)


result = fab(20)
if result != -1:
    print('总共有%d对小兔崽子诞生了！' % result)

# 分治思想
# 递归来做效率很低
