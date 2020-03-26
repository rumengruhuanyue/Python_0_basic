def discount(price, rate):
    final_price = price * rate
    # print('这里试图打印全局变量old_price的值：', old_price)
    old_price = 50
    print('修改后old_price的值1：', old_price)
    return final_price


old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discount(old_price, rate)
print('修改后old_price的值2：', old_price)
print('打折后的价格是：', new_price)
