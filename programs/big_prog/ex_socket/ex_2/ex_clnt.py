#!/usr/bin/python3

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from socket import *
import subprocess

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Chat_client:
	def __init__(self, ADDR):
		self.sock = socket(AF_INET, SOCK_STREAM) 
		self.sock.connect(ADDR)

	def send_msg(self, message):
		self.sock.send(b''+message)

	def print_msg(self):
		data = self.sock.recv(1024)
		data = '- ' + data.decode('utf8')
		subprocess.call(['echo', '-e', 
				u'\e[35m{}\e[0m'.format(data)])

	def exit(self):
		self.sock.close()



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	try:
		client = Chat_client(('localhost', 21567))
		print('Start client...')
		while True:
			msg = raw_input('> ')
			if not msg:
				break
			client.send_msg(msg)
			
			client.print_msg()

	except KeyboardInterrupt:
		print('Client stoped.')
		client.exit()
	finally:
		client.exit()
