#!/usr/bin/python

import socket
from findIP import Network

ip, neighbours = Network().networkscanner()
port = 12347

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(10)
c, addr = s.accept()
print('{} connected'.format(addr))

file_path = 'README4.md'
f = open(file_path, "wb")
chunk = c.recv(1024)
while chunk:
    f.write(chunk)
    chunk = c.recv(1024)

c.close()
s.close()