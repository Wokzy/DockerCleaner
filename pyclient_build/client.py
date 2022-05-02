import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 15250))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print(data) # ajobka 1 1 21212 1221 123
