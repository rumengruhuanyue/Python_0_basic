"""
创建 Twisted Reactor TCP 客户端 :Twisted Reactor 时间戳 TCP客户端
"""

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print('...sending %s...' % data)
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    """
    twisted.internet.protocol module： 这里继承自protocol.ClientFactory类。
            
        查看源码，这里定义了两个函数
        
        def clientConnectionFailed(self, connector, reason)
        def clientConnectionLost(self, connector, reason)
        
    -- lambda arguments : expression
    
    ---- A lambda function is a small anonymous function.
    ---- A lambda function can take any number of arguments, but can only have one expression.
        
        lambda self, connector, reason: reactor.stop()
        
        这里就是用到了传来的self, connector, reason，三个参数，执行reactor.stop()停止操作
    """
    # self.transport.loseConnection() ———— 上面关闭连接的语句会调用下面这个语句
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
