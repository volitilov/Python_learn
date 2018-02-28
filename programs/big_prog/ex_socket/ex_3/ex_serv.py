#!/usr/bin/python3

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from socketserver import (
	TCPServer as TCP,
	StreamRequestHandler as SRH
)
from time import ctime
import sys

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class MyTCPHandler(SRH):
	def handle(self):
		addr_1 = ' ' + str(self.client_address[0])
		addr_2 = ' ' + str(self.client_address[1])
		
		print('Connected client:' + addr_1 + addr_2)
		
		self.data = self.rfile.readline().strip()
		if not self.data:
			print(addr_1 + ':' + addr_2 + ' - disconnected')


		self.wfile.write(self.data)



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == "__main__":
	if len(sys.argv) < 3 or type(int(sys.argv[2])).__name__ != 'int':
		print('Usage: python ex_serv.py hostname port')
		sys.exit()
	else:
		ADDR = (sys.argv[1], int(sys.argv[2]))
		server =  TCP(ADDR, MyTCPHandler)

		try:
			print('Waiting for connection...')
			server.serve_forever()
		except KeyboardInterrupt:
			print('\nServer stoped.')
			server.server_close()