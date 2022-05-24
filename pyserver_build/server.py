#!/usr/bin/env python3
import socket, select

sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(5)
inputs = [sock]
outputs = []

messages = {}#1234

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
				print(f'Recieved {data.decode("ascii")} | from {s.getpeername()[0]}:{s.getpeername()[1]}\n')
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
		outputs.remove(s)
		s.send(messages[s])
		print(f'Sent {messages[s].decode("ascii")} | to {s.getpeername()[0]}:{s.getpeername()[1]}\n')

	for s in exceptional:
		if s in outputs:
			outputs.remove(s)
		inputs.remove(s)
		s.shutdown(socket.SHUT_RDWR)
		s.close()
		del messages[s]
