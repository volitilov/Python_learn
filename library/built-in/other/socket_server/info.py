socketserver ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Его назначение состоит в предоставлении большого объёма 
# стандартного кода, необходимого для создания сетевых клиентов и 
# серверов. Этот модуль обеспечивает создание от имени пользователя
# различных классов. 

# документация на английском:
# https://docs.python.org/3/library/socketserver.html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import socketserver as s

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

BaseServer(server_address, RequestHandlerClass)
# Содержит основные функциональные средства сервера и обра­ботчики 
# прерываний для промежуточных классов. Используется только для 
# порождения других классов, поэтому не приходится создавать 
# экземпляры данного класса. Вместо этого следует ис­пользовать класс 
# TCPServer или UDPServer

TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)
# Основной сетевой синхронный сервер ТCP

UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)
# Основной сетевой синхронный сервер UDP

UnixStreamServer(server_address, RequestHandlerClass, bind_and_activate=True)
# Основной синхронный сервер TCP на основе файлов

UnixDatagramServer(server_address, RequestHandlerClass, bind_and_activate=True)
# Основной синхронный сервер UDP на основе файлов

ForkingMixIn
ThreadingMixIn
# Предоставляет основные функциональные возможности вет­вления или 
# организации многопоточной работы. Используется только для создания 
# промежуточных классов, применяемых в сочетании с одним из 
# серверных классов для обеспечения опре­деленной асинхронности. 
# Непосредственное создание экзем­пляров этого класса не предусмотрено

ForkingTCPServer
ForkingUDPServer
# Сочетание ForkingMixin и TCPServer/UDPServer

ThreadingTCPServer(ThreadingMixIn, TCPServer)
ThreadingUDPServer(ThreadingMixIn, UDPServer)
# Сочетание ThreadingMixin и TCPServer/UDPServer

BaseRequestHandler
# Содержит основные функциональные средства обработки запросов на 
# обслуживание. Используется только для порожде­ния других классов, 
# поэтому в программах не создаются эк­земпляры данного класса. Вместо 
# этого следует использовать StreamRequestHandler или 
# DatagramRequestHandler

StreamRequestHandler
DatagramRequestHandler
# Реализация обработчика служб для серверов ТCP/UDP



# server objects :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
s = socketserver.BaseServer()

s.fileno()
# Вернёт дескриптор целочисленного файла для сокета, на котором прослушивает 
# сервер. Эта функция чаще всего передается селекторам, позволяя контролировать 
# несколько серверов в одном процессе.

s.handle_request()
# Обработать один запрос. Эта функция вызывает следующие методы:
#  get_request(), verify_request(), and process_request(). Если предоставленный 
# пользователем метод handle() класса обработчика вызывает исключение, вызывается 
# метод handle_error() сервера. Если запрос не будет получен в течение timeout 
# секунд, будет вызван handle_timeout(), и handle_request() вернёт ответ.

s.serve_forever(poll_interval=0.5)
# 

s.service_actions()
#

s.shutdown()
#

s.server_close()
#

s.address_family
#

s.RequestHandlerClass
#

s.server_address
#

s.socket
#

s.allow_reuse_address
#

s.request_queue_size
#

s.socket_type
#

s.timeout
#

s.finish_request(request, client_address)
#

s.get_request()
#

s.handle_error(request, client_address)
#

s.handle_timeout()
#

s.process_request(request, client_address)
#

s.server_activate()
#

s.server_bind()
#

s.verify_request(request, client_address)
#



# request handler objects :::::::::::::::::::::::::::::::::::::::::::::::
sb = socketserver.BaseRequestHandler

sb.setup()
#

sb.handle()
#

sb.finish()
#

