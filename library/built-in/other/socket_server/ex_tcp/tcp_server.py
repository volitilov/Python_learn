# В этом сценарии создаётся сервер TCP отметок времени с
# использованием классов SocketServer, TCPServer и 
# StreamRequestHandler

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from socketserver import (
	TCPServer as TCP,
	StreamRequestHandler as SRH
)
from time import ctime

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class MyTCPHandler(SRH):

	# перекрытие метода подкласса SRH. При получении сообщений от
	# клиента происходит вызов данного метода. В классе SRH сокеты
	# ввода и вывода расматриваются как объекты, подобные файлам,
	# поэтому в сценарии используются функции readline() для 
	# получения сообщения от клиента и функции write() для отправки
	# строки обратно клиенту
	def handle(self):
		self.data = self.rfile.readline().strip()
		print('...conected from:', self.client_address[0])

		# self.wfile.write(self.data)
		data = bytes('[{}] {}'.format(ctime(), 
			self.data), 'utf-8')
		self.wfile.write(data)



if __name__ == "__main__":
	HOST = ''
	PORT = 21567
	ADDR = (HOST, PORT)

	server =  TCP(ADDR, MyTCPHandler)
	# # создаётся сервер TCP на основе заданной информации о хосте и 
	# класса обработчика запросов
	
	try:
		print('Waiting for connection...')
		server.serve_forever()
		# переход в бесконечный цикл
	except KeyboardInterrupt:
		print('\nServer stoped.')
		server.server_close()