"""
创建 UDP 客户端 :

    cs = socket()                       # 创建客户端套接字
    comm_loop:                          # 通信循环
        cs.sendto()/cs.recvfrom()       # 对话（发送/接收）
    cs.close()                          # 关闭客户端套接字
"""
from socket import *

HOST = '127.0.0.1'
PORT = 21566
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data1, addr = udpCliSock.recvfrom(BUFSIZ)
    if not data1:
        break
    print(data1.decode('utf-8'))

udpCliSock.close()
