#!/usr/bin/python3

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import socket, sys
import threading as th

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class ChatServer(th.Thread):
	def __init__(self, *args):
		self.ADDR = args
		th.Thread.__init__(self)
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.users = []
		
		try:
			self.server.bind(self.ADDR)
		except socket.error:
			print('Bind failed %s' % (socket.error))
			sys.exit()

		self.server.listen(10)


	def exit(self):
		self.server.close()
		

	def run_thread(self, conn, addr):
		cl_addr = ' ' + addr[0] + ':' + str(addr[1])
		th_name = ' ' + th.current_thread().getName()

		print('Connected client:' + cl_addr + th_name)

		while True:
			data = conn.recv(1024)
			if not data:
				print(str(addr[0]) + ':' + str(addr[1]) + ' - disconnected')
				for user in self.users:
					if user[0] == conn:
						self.users.remove(user)
				break

			reply = b'' + data
			for user in self.users:
				if user[0] != conn:
					user[0].sendall(reply)
			 
		conn.close()

	def run(self):
		print('Waiting for connections on port %s' % (self.ADDR[1]))
		while True:
			conn, addr = self.server.accept()
			self.users.append((conn, addr))
			th.Thread(target=self.run_thread, args=(conn, addr)).start()






# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  
if __name__ == '__main__':
	if len(sys.argv) < 3 and type(int(sys.argv[2])).__name__ != 'int':
		print('Usage: python ex_serv.py hostname port')
		sys.exit()
	else:
		try:
			server = ChatServer(sys.argv[1], int(sys.argv[2]))
			server.run()
		except KeyboardInterrupt:
			server.exit()
