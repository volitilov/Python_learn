from socket import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# cs = socket()
# # создание сокета клиента
# cs.connect()
# # осуществление попытки установить соединение с сервером

# while True:
# # цикл связи
# 	cs.send()/cs.recv()
# 	# ведение деолога (передача/приём)

# cs.close()
# # закрытие сокета клиента 



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# в этом сценарии создаётся клиент TCP, который формирует 
# запросы пользовате­лю на получение сообщений, подлежащих 
# отправке на сервер, получает эти сообще­ния от сервера с 
# префиксом в виде отметки времени, а затем отображает 
# результаты для пользователя.

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
tcp_cli_sock.connect(ADDR)

while True:
	data = input('> ')
	if not data:
		break
	tcp_cli_sock.send(bytes(data, 'utf-8'))
	data = tcp_cli_sock.recv(BUFSIZ)
	if not data:
		break
	print(data.decode('utf-8'))

tcp_cli_sock.close()
