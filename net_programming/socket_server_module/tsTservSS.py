"""
创建 SocketServer TCP 服务器:SocketServer 时间戳 TCP 服务器
"""
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        """
        当接收到一个来自客户端的消息时，它就会调用 handle()方法。
        而 StreamRequestHandler 类将输入和输出套接字看作类似文件的对象，
        因此我们将使用 readline()来获取客户端消息,并利用 write()将字符串发送回客户端
        """
        data = self.rfile.readline().decode('utf-8')
        self.wfile.write(('[%s] %s' % (ctime(), data)).encode('utf-8'))


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
# 无限循环地等待并服务于客户端请求。
tcpServ.serve_forever()
