#!/usr/bin/env python3
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 15250))
sock.listen(1)
conn, addr = sock.accept()

#test comment
print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()

#p10273.3 12312313 8 12
