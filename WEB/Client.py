__author__ = 'Yue'
import socket

port = 8080
host = "localhost"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Hello".encode("ascii"),(host, port))
