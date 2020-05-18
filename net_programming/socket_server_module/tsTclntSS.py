"""
创建 SocketServer TCP 客户端 : SocketServer 时间戳 TCP 客户端
"""
from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break

    """
    因为这里使用的处理程序类对待 套接字通信就像文件一样，
    所以必须发送行终止符（回车和换行符）。
    """
    tcpCliSock.send(('%s\r\n' % data).encode('utf-8'))

    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    #     str.strip([chars])  # 其中[chars]可选参数，表示去除开头和结尾处的所有的[chars]字符；若未加参数，默认去除空格或者换行符
    #     在这里未加参数，末尾的\r\n可去除
    print(data.strip().decode('utf-8'))
    """
    SocketServer 请求处理程序的默认行为是接受连接、获取请求，然后关闭连接。
    由于这个原因，我们不能在应用程序整个执行过程中都保持连接，
    因此,每次向服务器发送消息时，都需要创建一个新的套接字。
    """
    tcpCliSock.close()


"""
rs:
——————————
client:
    > start
    [Mon May 18 16:34:51 2020] start
    >     end
    [Mon May 18 16:34:55 2020]     end
    > 

    Process finished with exit code 0
server:
    waiting for connection...
    ...connected from: ('127.0.0.1', 56982)
    ...connected from: ('127.0.0.1', 56992)
    ...connected from: ('127.0.0.1', 56998)
"""