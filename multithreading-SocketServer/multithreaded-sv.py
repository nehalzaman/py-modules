#!/usr/bin/python

import SocketServer

class threadedTcpServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer): pass

class handler(SocketServer.BaseRequestHandler):
	def handle(self):
		print '[*] Got connection from : ',self.client_address
		message = 'dummy'
		while message:
			message = self.request.recv(2048)
			print '[*] Client typed : %s'%message
                        self.request.send('You typed : '+message)
		print '[*] Connection closed...'

serverAddr = ('127.0.0.1',12345)
server = threadedTcpServer(serverAddr, handler)
server.serve_forever()
