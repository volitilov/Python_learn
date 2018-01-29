from socket import *
from time import ctime

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# ss = socket()
# # создание сокета сервера
# ss.bind()
# # привязка сокета сервера
# while True:
# # бесконечный цикл сервера
# 	cs = ss.recvfrom()/ss.sendto()
# 	# диалоговое окно (параметры приёма/передачи)
# ss.close()


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# в этом сценарии создаётся сервер UDP, который принимает
# сообщения от клиентов и возвращает их с префиксом в виде
# времени

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

HOST = ''
# переменная песта, это указывает на то, что в методе bind()
# может использоваться любой доступный адрес 
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_ser_sock = socket(AF_INET, SOCK_DGRAM)
udp_ser_sock.bind(ADDR)

try:
	while True:
		print('UDP сервер запущен...')
		data, addr = udp_ser_sock.recvfrom(BUFSIZ)
	
		data = data.decode('utf-8')
		data = bytes('[{}], {}'.format(ctime(), data), 'utf-8')
		udp_ser_sock.sendto(data, addr)
		print('Сообщение полученно, обработано и отправленно для:', addr)

except KeyboardInterrupt:
	print('Сервер остановлен.')
	udp_ser_sock.close()
