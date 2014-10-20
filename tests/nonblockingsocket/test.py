#!/usr/bin/env python3
#encoding: utf-8

import socket
import time
import sys
from gui import *
import math


if __name__ == "__main__":
    sel = input("Server (s) or client (c)? ")

    if str(sel) == "s":
        # Servertest
        try:
            HOST = "0.0.0.0"
            PORT = 22500

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((HOST, PORT))
            sock.setblocking(0)

            gui = GUI()
            gui.createWindow('Server')

            # Get initial time
            now = time.clock()
            lastNw, lastF = 0.0, 0.0
            nwLimit = 1 # Check network every 200ms
            # Server main loop
            while True:
                now = time.clock()
                # Networking
                if (now - lastNw) > (nwLimit/100):
                    lastNw = now
                    while True:
                        try:
                            data, addr = sock.recvfrom(1400)
                            print(addr[0], data, "end")
                        except Exception as e:
                            # No data waiting, break fetch-loop
                            data, addr = None,None
                            break

                # Calculate FPS
                print("FPS:" + str(1/(now-lastF)) + "\r",end="")
                lastF = now

                gui.update()
        finally:
            sock.close()
        
    elif str(sel) == "c":
        HOST = "127.0.0.1"
        PORT = 22500

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Client main loop
            data = ""
            while str(data) != "end":
                data = input("> ")
                sock.sendto(bytes(data, "utf-8"), (HOST, PORT))
        finally:
            sock.close()
        