# coding: utf8

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from socket import *
import subprocess

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)



try:
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(ADDR)
	print('Start client...')
	while True:
		# отправка сообщения на сервер
		msg = raw_input('> ')
		if not msg:
			break
		sock.send(bytes(msg))

		# получение сообщений с сервера
		data = sock.recv(BUFSIZ)
		if not data:
			break
		data = '- ' + data.decode('utf8')
		subprocess.call(['echo', '-e', 
				u'\e[35m{}\e[0m'.format(data)])

except KeyboardInterrupt:
	print('Client stoped.')
	sock.close()
