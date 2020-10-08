#!/usr/bin/python

import socket
import threading

class myThread(threading.Thread):
	def __init__(self, clientSocket, clientAddr):
		threading.Thread.__init__(self)
		self.clientSocket = clientSocket
		self.clientAddr = clientAddr

	def run(self):
		self.clientSocket.send('Welcome to my Server...\n')
		print 'Connection : ' + str(clientAddr[0]) + ' at ' + str(clientAddr[1])
		message = 'dummy'
		while message:
			message = self.clientSocket.recv(2048)
			print str(clientAddr[0]) + ' typed : ' + message
			self.clientSocket.send('You typed : ' + message)
		print 'Connection closed.\n'

serverAddr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverAddr.bind(('127.0.0.1',12345))
print 'Server started...'

while True:
	serverAddr.listen(1)
	clientSocket, clientAddr = serverAddr.accept()
	newThread = myThread(clientSocket, clientAddr)
	newThread.start()
