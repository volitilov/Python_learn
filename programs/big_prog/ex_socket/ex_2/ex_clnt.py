#!/usr/bin/python3

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import subprocess, sys
from select import select
from socket import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Chat_client:
	def __init__(self, ADDR):
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.settimeout(2)

		try:
			self.sock.connect(ADDR)
		except:
			sys.exit()

		sys.stdout.write('> '); sys.stdout.flush()

		while True:
			socket_list = [sys.stdin, self.sock]
			ready_to_read, _, _ = select(socket_list , [], [])

			for sock in ready_to_read:
				if sock == self.sock:
					self.print_msg()
				else:
					msg = sys.stdin.readline()
					self.send_msg(msg)
					sys.stdout.write('> '); sys.stdout.flush()

	def send_msg(self, message):
		self.sock.send(message)

	def print_msg(self):
		data = self.sock.recv(4096)
		if not data:
			sys.exit()
		else:
			data = '- ' + data
			subprocess.call(['echo', '-e', 
					u'\e[35m{}\e[0m'.format(data)])
			sys.stdout.write('> '); sys.stdout.flush()

	def exit(self):
		self.sock.close()



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	if len(sys.argv) < 3 and type(int(sys.argv[2])).__name__ != 'int':
		print('Usage: python ex_clnt.py hostname port')
		sys.exit()
	else:
		try:
			host = sys.argv[1]
			port = int(sys.argv[2])

			print('Start client...')
			client = Chat_client((host, port))

		except KeyboardInterrupt:
			print('Client stoped.')
			client.exit()
		finally:
			sys.exit()

