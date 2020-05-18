from socket import *
from time import ctime

"""
 tsTserv.py 文件，它是一个 TCP 服务器程序，它接受客户端发送的数据字符串，
 并将其打上时间戳（格式：[时间戳]数据）并返回给客户端
 （“tsTserv”代表时间戳 TCP 服务器，其他文件以类似的方式命名）。

 伪码：
 ss = socket()                      # 创建服务器套接字 
 ss.bind()                          # 套接字与地址绑定 
 ss.listen()                        # 监听连接 
 inf_loop:                          # 服务器无限循环     
    cs = ss.accept()                # 接受客户端连接    
    comm_loop:                      # 通信循环         
        cs.recv()/cs.send()         # 对话（接收/发送）     
    cs.close()                      # 关闭客户端套接字 
 ss.close()                         # 关闭服务器套接字 #（可选） 
 
 首先启动服务器（在任何客户端试图连接之前）。
"""

HOST = ''  # HOST 变量是空白的，这是对 bind()方法的标识，表示它可以使用任何可用的地址
PORT = 21576
BUFSIZ = 1024  # 1kb ，1024 bites 缓冲区大小设置为 1KB.可以根据网络性能和程序需要改变这个容量
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)  # listen() 方法的参数是在连接被转接或拒绝之前，传入连接请求的最大数。

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        # # # 在网络传输中，以二进制传输
        # 0. data：接收到客户端发送的的二进制数据
        # 1. 先将data进行解码——>str
        # 2. 然后，拼接要发送给客户端的数据(str)
        # 3. 进行编码——>bytes ,转换成二进制数据，传输给客户端
        #      3.1 实现方式可以使用bytes(data,'utf-8')/data.encode('utf-8')
        # 4. 客户端获取到了数据，解码，即得到服务器发送的原始数据！

        # tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
        tcpCliSock.send(('[%s] %s' % (ctime(), data.decode('utf-8'))).encode('utf-8'))

    tcpCliSock.close()
tcpSerSock.close()  # : This inspection detects code which can not be normally reached.
