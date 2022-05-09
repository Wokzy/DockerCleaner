#!/usr/bin/env python3
import socket, select

sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(5)
inputs = [sock]
outputs = []

messages = {}

print('binded')


while inputs:
	readable, writable, exceptional = select.select(inputs, outputs, inputs)

	for s in readable:
		if s == sock:
			conn, addr = s.accept()
			conn.setblocking(0)
			inputs.append(conn)
		else:
			data = s.recv(1024)
			
			if data:
				messages[s] = data.upper()
				if s not in outputs:
					outputs.append(s)
			else:
				if s in outputs:
					outputs.remove(s)
				inputs.remove(s)
				s.shutdown(socket.SHUT_RDWR)
				s.close()
				del messages[s]

	for s in writable:
		print(s)
		outputs.remove(s)
		s.send(messages[s])

	for s in exceptional:
		if s in outputs:
			outputs.remove(s)
		inputs.remove(s)
		s.shutdown(socket.SHUT_RDWR)
		s.close()
		del messages[s]
