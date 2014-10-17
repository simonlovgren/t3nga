#!/usr/bin/env python3
import socket
import sys
import re

# Base communications class
class BaseSocket:
    # Set up baseSocket. Returns FALSE on error
    def __init__(self, port = 22500):
        # Set base vals
        self.FAMILY = socket.AF_INET
        self.TYPE = socket.SOCK_STREAM
        self.HOST = "0.0.0.0"
        self.PORT = port

        # Set up socket
        try:
            self.socket = socket.socket(self.FAMILY, self.TYPE)
        except OSError as msg:
            print("Could not create socket")
            return False

    # Close connection
    def close(self):
        self.socket.close()

## Server Socket ##
class MasterSocket(BaseSocket):

    # Set up listening to socket. Returns BOOLEAN
    def listen(self, whiteListIP = None, backlog = 1):
        # Check for whitelist IP
        self.HOST = "0.0.0.0"
        if whiteListIP != None:
            self.HOST = whiteListIP

        # try binding socket and start listening
        try:
            self.socket.bind((self.HOST, self.PORT))
            self.socket.listen(backlog)
        except OSError as msg:
            self.socket.close()
            return False
        return True

    # Returns BOOLEAN
    def startAcceptingClient(self):
        try:
            self.conn, self.addr = self.socket.accept()
        except OSError as msg:
            return False
        return True

    # Send data to connected computer. Return BOOLEAN
    def send(self, message):
        try:
            self.conn.send(message)
        except OSError as msg:
            return False
        return True

    # Recieve (wait for) data from connection. Data if OK, FALSE if error
    def recieve(self, buff = 1024):
        try:
            data = self.conn.recv(buff)
        except OSError as msg:
            return False
        return data

## Client Socket ##
class SlaveSocket(BaseSocket):

    # Connect to server. Returns BOOLEAN
    def connect(self, ip):
        self.HOST = ip
        try:
            self.socket.connect((self.HOST, self.PORT))
        except OSError as msg:
           self.HOST = "0.0.0.0"
           return False
        return True

    # Send data to server. Return BOOLEAN
    def send(self, message):
        try:
            message = bytes(message, "utf-8")
            self.socket.send(message)
        except OSError as msg:
            return False
        return True

    # Recieve (wait for) data from server. Data if OK, FALSE if error
    def recieve(self, buff = 1024):
        try:
            data = self.socket.recv(buff)
        except OSError as msg:
            return False
        return data



####### TEST FUNCTIONS ##########
def isPort(test):
    try:
        return (test > 0 and test < 999999)
    except Exception:
        return False

def isIP(test):
    regx = r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}'
    return re.match(regx, test) != None

###### TEST ######
if __name__ == "__main__":

    sel = None
    while sel != "s" and sel != "c":
        sel = input('server (s) or client (c)?')
        print(sel)

    # Evaluate selection
    ### Server
    if sel == "s":
        # Start creating server
        print("\r\nSetting up SERVER\r\n--------------------")
        
        # Start listening on port
        portSelected = False
        while not portSelected:
            port = 0
            while not isPort(port):
                if port != None:
                    print("Invalid port!")
                port = int(input("Please select a port: "))

            # Try connecting to port
            sock = MasterSocket(port)
            if sock:
                portSelected = True
            else:
                print("Port taken...")

        print("Trying to start listening")
        
        listening = False
        tries = 3
        while not listening and tries > 0:
            # Try connecting to port
            listening = sock.listen()
            if not listening:
                print("Listen failed (" + str(tries) + ")")
                tries -= 1

        if not listening:
            print("Could not start server. Exiting.")
            sock.close()
            sys.exit(1)

        print("Started listening")

        # Try start to accept clients
        print("Trying to start accepting clients")
        accept = False
        tries = 3
        while not accept and tries > 0:
            # Try connecting to port
            accept = sock.startAcceptingClient()
            if not accept:
                print("Listen failed (" + str(tries - (tries-1)) + ")")
                tries -= 1

        if not accept:
            print("Could not start accepting clients. Exiting.")
            sock.close()
            sys.exit(1)

        print("Accepting clients")

        print("Waiting for connection")

        while listening:
            data = sock.recieve() # Retrieve data
            print(data.decode('utf-8'))
            sock.send(data) # Send data back
            # Evaluate kill command
            if data.decode('utf-8') == "killserver":
                listening = False

        sock.close()



    ###  Client
    if sel == "c":
        # Start creating server
        print("\r\nSetting up CLIENT\r\n--------------------")
        
        # Start listening on port
        sockLock = False
        while not sockLock:
            ip = ""
            while not isIP(ip):
                if ip != None:
                    print("Invalid IP!")
                ip = input("Please select an IP: ")

            port = None
            while not isPort(port):
                if port != None:
                    print("Invalid port!")
                port = int(input("Please select a port: "))

            # Try connecting to port
            sock = SlaveSocket(port)
            if sock:
                sockLock = True
            else:
                print("Port taken...")

        # Connect to serve
        connected = False
        tries = 3
        while not connected and tries > 0:
            # Try connecting to port
            connected = sock.connect(ip)
            if not connected:
                print("Connection failed to " + ip + " (" + str(tries - (tries-1)) + ")")
                tries -= 1

        if not connected:
            print("Could not connect to server. Exiting.")
            sock.close()
            sys.exit(1)

        while connected:
            tosend = input("Write data to send:")
            # Evaluate kill command
            if tosend == "disconnect":
                break
            sock.send(tosend) # Send data
            data = sock.recieve()
            print("Response: " + data.decode("utf-8"))
        print("Closing connection")
        sock.close()






# print("IS IP (fail): " + str(isIP("192.168.a.20")))
# print("IS IP (Success): " + str(isIP("192.168.1.20")))

# print("IS Port (fail): " + str(isPort("s5844")))
# print("IS Port (Success): " + str(isPort(55245)))
# print("IS Port (Success): " + str(isPort(int(input("Manual port")))))

'''
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
'''