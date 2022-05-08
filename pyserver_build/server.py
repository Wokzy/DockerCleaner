#!/usr/bin/env python3
import socket

sock = socket.socket()
sock.bind(('localhost', 1234))
print('binded')
sock.listen(1024)

while True:
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
