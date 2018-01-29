from socket import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# cs = socket()
# # создание сокета клиента

# while True:
# # цикл связи
# 	cs.sendto()/cs.recvfrom()
# 	# ведение деолога (передача/приём)

# cs.close()
# # закрытие сокета клиента 



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# в этом сценарии создаётся клиент UDP, который формирует 
# запросы пользовате­лю на получение сообщений, подлежащих 
# отправке на сервер, получает эти сообще­ния от сервера с 
# префиксом в виде отметки времени, а затем отображает 
# результаты для пользователя.

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_cli_sock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = input('> ')
	if not data:
		break
	udp_cli_sock.sendto(bytes(data, 'utf-8'), ADDR)
	data, ADDR = udp_cli_sock.recvfrom(BUFSIZ)
	if not data:
		break
	print(data.decode('utf-8'))

udp_cli_sock.close()
