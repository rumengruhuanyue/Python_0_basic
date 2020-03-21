import random
secret = random.randint(1,10)
# print(secret)
print("----------文字游戏升级--------------")
flag = 0
temp = input('请猜测一个1-10间的数字:')
guess = int(temp)
flag = flag + 1

if guess == secret :
    print('猜对了！')
else:
    if guess > secret :
        print('哥，大了大了！')
    else : 
        print('哥，小了！')
    while flag < 3:
        temp = input('猜错了，请猜重新测一个数字:')
        guess = int(temp)
        if guess == secret :
            print('猜对了！')
        else:
            if guess > secret :
                print('哥，大了大了！')
            else : 
                print('哥，小了！')
        flag = flag + 1    
print('游戏结束')
