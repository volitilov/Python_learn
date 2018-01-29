# Это - код клиента TCP отметок времени, который предназначен
# для обмена данными с файлоподобными объектами 
# StreamRequestHandler класса SocketServer

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from socket import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PORT = 21567
HOST = 'localhost'
BUFSIZ = 1024
ADDR = (HOST, PORT)

	
while True:
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(ADDR)

	data = input('> ')
	if not data:
		break

	sock.sendall(bytes(data + '\n', "utf-8"))

	received = str(sock.recv(BUFSIZ), "utf-8")
	if not received:
		break
	print(received)

	sock.close()