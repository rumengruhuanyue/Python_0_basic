from socket import *

"""
 伪码：
 cs = socket()               # 创建客户端套接字 
 cs.connect()                # 尝试连接服务器
 comm_loop:                  # 通信循环     
    cs.send()/cs.recv()      # 对话（发送/接收） 
 cs.close()                  # 关闭客户端套接字
"""
# 使用相同的计算机，但是完全可以使用另一台主机运行服务器。如果是这种情况，仅仅需要修改主机名就可以了
HOST = '127.0.0.1'  # or 'localhost'

PORT = 21576
BUFSIZ = 1024   # 缓冲区大小设置为 1KB
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # 分配了 TCP 客户端套接字（tcpCliSock）
tcpCliSock.connect(ADDR)   # 主动调用并连接到服务器。

while True:
    data = input('> ')
    # print(data)
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()

