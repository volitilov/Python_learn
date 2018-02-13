from socket import *
from time import ctime

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# tcp_sock = socket(family=AF_INET, type=SOCK_STREAM)
# пример создания TCP сокета
# udp_sock = socket(family=AF_INET, type=SOCK_DGRAM)
# пример создания UDP сокета


# ss = socket()
# # создание сокета сервера

# ss.bind()
# # Для привязки используется функция bind сокета, которая 
# # принимает массив, содержащий два элемента: хост и порт.

# ss.listen()
# # прослушивание запросов на соединение
# 	while True:
#	# бесконечный цикл сервера
#		cs, addr = ss.accept()
#		# принимаем соединения с помощью функции accept. 
#		# Она ждёт появление входящего соединения и возвращает 
#		# связанный с ним сокет и адрес подключившегося. 
#		# Адрес — массив, состоящий из IP-адреса и порта.
# 		while True:
# 		# цикл связи
# 			cs.recv()/cs.send()
# 			# диалоговое окно (параметры приёма/передачи)
# 		cs.close()
# 		# закрытие сокета клиента
# ss.close()
# # закрытие сокета сервера (необязательно)




# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# в этом сценарии создаётся сервер TCP, который принимает
# сообщения от клиентов и возвращает их с префиксом в виде
# времени

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

HOST = ''
# Если не указать хост или указать "0.0.0.0", сокет будет 
# прослушивать все хосты. Если указать "127.0.0.1", то 
# подключиться можно будет только с этого же компьютера.
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_ser_sock = socket(AF_INET, SOCK_STREAM)
tcp_ser_sock.bind(ADDR)
tcp_ser_sock.listen(5)
# установление максимального количества запросов

try:
	while True:
		print('Ожидается соединение...')
		tcp_cli_sock, addr = tcp_ser_sock.accept()
		print('...соединён с:', addr)

		while True:
			data = tcp_cli_sock.recv(BUFSIZ)
			if not data:
				break
			data = data.decode('utf-8')
			data = bytes('[{}], {}'.format(ctime(), data), 'utf-8')
			tcp_cli_sock.send(data)

		tcp_cli_sock.close()
except KeyboardInterrupt:
	print('Сервер остановлен.')
	tcp_ser_sock.close()
