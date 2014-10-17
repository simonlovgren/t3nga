#!/usr/bin/env python3
import socket
import sys
#import http.server

#WIP#
class NetworkListener:
    
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.listen()
        
    def listen(self):
        # Collect latest data and update data variable
        self.data = "Simulated data"
        print("Listening")
    
    def getData(self):
        return self.data
    
#nl = NetworkListener("192.168.1.23", "22500");
#print(nl.getData())


## Taken from: https://docs.python.org/3.1/howto/sockets.html
class mysocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        msg = ''
        while len(msg) < MSGLEN:
            chunk = self.sock.recv(MSGLEN-len(msg))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            msg = msg + chunk
        return msg
s = mysocket()
s.connect("130.238.95.2", 22500)
mysend("hej simon")

print(myreceive())