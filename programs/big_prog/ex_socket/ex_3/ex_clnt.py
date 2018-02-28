#!/usr/bin/python3

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from socket import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PORT = 21567
HOST = 'localhost'
BUFSIZ = 1024
ADDR = (HOST, PORT)

	
while True:
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(ADDR)

	data = raw_input('> ')
	if not data:
		break

	sock.sendall(bytes(data + '\n'))

	received = u''+sock.recv(BUFSIZ)
	if not received:
		break
	print(received)

	sock.close()