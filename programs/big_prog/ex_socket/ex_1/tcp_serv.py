# coding: utf8

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from socket import *
import subprocess

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(ADDR)
sock.listen(1)

try:
	print('\nstart server.............................\n')
	while 1:
		conn, addr = sock.accept()
		print(str(addr[0]) + ':' + str(addr[1]) + ' - connected')

		while True:
			# получение и распечатка сообщений от клиента
			data = conn.recv(BUFSIZ)
			if not data:
				print(str(addr[0]) + ':' + str(addr[1]) + ' - disconnected')
				break
			data = '- ' + data.decode('utf-8')
			subprocess.call(['echo', '-e', 
					u'\e[35m{}\e[0m'.format(data)])
		
			# отправка сообщений клиенту
			msg = raw_input('> ')
			if not msg:
				break
			conn.send(bytes(msg))

		conn.close()
except KeyboardInterrupt:
	print('\nServer stoped............................\n')
	sock.close()
finally:
	sock.close()
