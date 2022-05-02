import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 15250))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print data