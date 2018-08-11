import socket

#创建套接字
serSocket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#插入一个电话卡
serSocket.bind(("",9900))

#设置为响铃模式
serSocket.listen(5)

#准备接电话
while True:
	cliSocket,cliInfo = serSocket.accept()

	#和这个电话进行收发数据
	while True:
		recvData = cliSocket.recv(1024)

		if len(recvData)>0:
			print("%s:%s"%(str(cliInfo),recvData.decode("gb2312")))
		else:
			break

		sendData = input('输入发送给%s的数据:'%(str(cliInfo)))
		cliSocket.send(sendData.encode("gb2312"))

	cliSocket.close()

serSocket.close()
