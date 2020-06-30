#!/usr/bin/python

import socket
from findIP import Network

ip, neighbours = Network().networkscanner()
port = 12347

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

file_path = 'README.md'
f = open(file_path, "rb")
chunk = f.read(1024)
while chunk:
   s.send(chunk)
   chunk = f.read(1024)

f.close()
s.close()