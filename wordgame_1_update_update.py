import random
secret = random.randint(1,10)
# print(secret)
print("----------文字游戏升级--------------")
flag = 0
while flag < 3 :
    temp = input('请猜测一个1-10间的数字:')
    guess = int(temp)
    if guess == secret :
        print('猜对了！')
        break # 如果猜对了，跳出循环
    else:
        if guess > secret :
            print('哥，大了大了！')
        else :
            print('哥，小了！')
    flag = flag + 1
print('游戏结束')
