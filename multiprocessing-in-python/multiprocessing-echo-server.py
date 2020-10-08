#!/usr/bin/python

import socket
import multiprocessing

def myfunc(i, clientSock, clientAddr):
	print '[*] Process %d active.'%i
	print '[*] Got connection from '+str(clientAddr[0])+' at port '+str(clientAddr[1])
	message = 'dummy'
	while message:
		clientSock.send('Enter a string : ')
		message = clientSock.recv(2048)
		clientSock.send('You entered : '+message)
	print '[*] Connection closed with '+str(clientAddr[0])

servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servSock.bind(('127.0.0.1', 12345))
i = 1

while True:
	servSock.listen(1)
	clientSock, clientAddr = servSock.accept()
	p = multiprocessing.Process(target = myfunc, args = (i, clientSock, clientAddr))
	i = i + 1
	p.start()
