"""
创建 UDP 服务器: UDP 是无连接的，所以这里没有调用“监听传入的 连接”

    ss = socket()                       # 创建服务器套接字
    ss.bind()                           # 绑定服务器套接字
    inf_loop:                           # 服务器无限循环
        cs = recvfrom()/ss.sendto       # 关闭（接收/发送）
    ss.close()                          # 关闭服务器套接字
"""
from socket import *
from time import ctime

HOST = ''
PORT = 21566
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('wait for message...')  # 。注意，此时消息并不是“waiting for connection”，而是“waiting for message”!
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('[%s] %s' % (ctime(), data.decode('utf-8'))).encode('utf-8'), addr)
    # print('...received from and returned to:', addr[0])
    print('...received from and returned to:', addr)

udpSerSock.close()  # This inspection detects code which can not be normally reached.
