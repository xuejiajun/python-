import socket 

#建立一个套接字（买个手机）
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定ip 和 端口为5555 (插入一个手机卡)
serverSocket.bind(("",5555))

#设置为监听模式
serverSocket.listen(5)

#准备接听（准备接电话）
#clientSocket 表示这个新的客户端 类似用户给10086打电话，10086会分配一个新的客服妹妹给我
#clientInfo 是对方的 Ip 和 Port

clientSocket,clientInfo = serverSocket.accept()

#serverSocket 只负责接听，clientSocket负责接收数据
recvData = clientSocket.recv(1024)

print("%s:%s"%(str(clientInfo),recvData.decode('gb2312')))

clientSocket.close()
serverSocket.close()
