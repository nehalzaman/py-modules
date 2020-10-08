#!/usr/bin/python

import SocketServer

class myserver(SocketServer.ForkingMixIn, SocketServer.TCPServer): pass

class handler(SocketServer.BaseRequestHandler):
    def handle(self):
        print '[*] Got connection from : ',self.client_address
        self.request.send('Enter your name : ')
        name = self.request.recv(2048).split('\n')[0]
        message = 'dummy'
        while message:
            self.request.send(name+' : ')
            message = self.request.recv(2048)
            print name + ' : '+message
            self.request.send(name +' typed : '+message)
        print '[*] Connection closed...'
        print '[*] Bye '+name

server = myserver(("127.0.0.1",12345), handler)
server.serve_forever()
