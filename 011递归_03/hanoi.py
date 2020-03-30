def hanoi(n, x, y, z):      # n层从x经过y移动到z
    if n == 1:
        print(x + '——>' + z)   # 递归初始条件
    else:
        hanoi(n-1, x, z, y)    # 先将n-1层从x经过z移动到y，这里直接回调就行
        print(x + '——>' + z)   # 将最底下的最后一个盘子从x移动到z上
        hanoi(n-1, y, x, z)    # 再将n-1层从现在的y位置经过x移动到z，同理，这里直接回调就行


num = int(input('请输入汉诺塔层数：'))
hanoi(num, 'X', 'Y', 'Z')


# http://www.hannuota.cn/
# hanoi在线游戏
