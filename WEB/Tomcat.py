__author__ = 'Yue'

# UDP not tcp

import socket

port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
while True:
    data,attr = s.recv(1024)
    print("Received:"+data)
