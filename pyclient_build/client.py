import socket, time
from datetime import datetime

sock = socket.socket()
sock.connect(('localhost', 1234))

c = datetime.now()

while (datetime.now() - c).total_seconds() < 61:
	time_passed = int((datetime.now() - c).total_seconds())
	if time_passed % 5 == 0:
		sock.send(bytes(f'time passed: {time_passed}\n'.encode('ascii')))
		print(sock.recv(1024).decode('ascii'))
		time.sleep(1)


sock.shutdown(socket.SHUT_RDWR)
time.sleep(0.1)
sock.close()