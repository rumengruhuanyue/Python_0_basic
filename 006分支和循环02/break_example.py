bingo = 'Python'
answer = input('目前在学哪门语言：')

while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入（答案正确才能退出游戏）：')

print('哟哟，不错哦！')
print('游戏结束')
