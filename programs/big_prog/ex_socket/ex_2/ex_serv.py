#!/usr/bin/python3

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import socket, sys
from threading import Thread

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class ChatServer(Thread):
	def __init__(self, *args):
		self.ADDR = args
		Thread.__init__(self)
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.users = {}
		
		try:
			self.server.bind(self.ADDR)
		except socket.error:
			print('Bind failed %s' % (socket.error))
			sys.exit()

		self.server.listen(10)


	def exit(self):
		self.server.close()

	def run_thread(self, conn, addr):
		print('Client connected with ' + addr[0] + ':' + str(addr[1]))
		while True:
			data = conn.recv(1024)
			if not data:
				print(str(addr[0]) + ':' + str(addr[1]) + ' - disconnected')
				break
			reply = b'' + data
			conn.sendall(reply) 
			 
		conn.close()

	def run(self):
		print('Waiting for connections on port %s' % (self.ADDR[1]))
		while True:
			conn, addr = self.server.accept()
			Thread(target=self.run_thread, args=(conn, addr)).start()




# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  
if __name__ == '__main__':
	try:
		server = ChatServer('', 21567)
		server.run()
	except KeyboardInterrupt:
		server.exit()