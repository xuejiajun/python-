import socket

#在客户端中套接字只有一个，在服务器中有两个套接字
#一个用来接听的套接字，一个是新创建的客户端的套接字

#创建套接字
clientSocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

"""
注意：
1-tcp 客户端已经链接好了服务器，所以在以后的数据发送中，不需填写对方的ip 和 port ----打电话
2-udp 在发送数据的时候，因为没有之前的链接，所以需要在每次的发送中都要添加接收方的 ip 和 port---写信
"""

#链接谁，等着谁给发送数据
clientSocket.connect(("192.168.204.1",8989))

#发送数据
clientSocket.send("hahha".encode("gb2312"))

#接受数据
recvData = clientSocket.recv(1024)

print("recvData = %s"%(recvData).decode("gb2312"))

#关闭套接字
clientSocket.close()

