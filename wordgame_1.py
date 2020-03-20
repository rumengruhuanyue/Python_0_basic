print("--------------第一个Pyhon文字小游戏----------------")
temp = input("不妨猜一下现在我心里想的数字：")
print(temp)
guess = int(temp)
if guess == 8:
    print("呦呵，你是我肚子里面的蛔虫吗？")
    print("哈哈，猜中也没有奖励！")
else:
    print("猜错了，我现在心里想的是数字8！")
print("游戏结束，不玩啦^_^ ")
