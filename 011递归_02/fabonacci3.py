def fab(n):
    x = [0]
    x = x * n
    x[0] = 1
    x[1] = 1
    for i in range(2, n):   # range不包含n，正好脚标从0开始
        x[i] = x[i - 1] + x[i - 2]
    return x[n-1]


result = fab(20)
print('总共有%d对小兔崽子诞生！' % result)

# 使用list容器迭代，空间复杂度较高

