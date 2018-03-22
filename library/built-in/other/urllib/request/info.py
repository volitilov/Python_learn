urllib.request ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Этот модуль предоставляет расширенные возможности для получения 
# информа­ции из Интернета. Поддерживаются автоматические перенаправления 
# при получении заго­ловка Location, возможность аутентификации, обработка 
# cookies и др.

# документация на английском:
# https://docs.python.org/3/library/urllib.request.html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from urllib.request import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, 
	cadefault=False, context=None)
# выполнения запроса. 
# В первом параметре задается полный URL-aдpec или объект, возвращаемый 
# конструктором класса Request. Запрос выполняется методом GET, если данные 
# не указаны во втором пара­метре, и методом Роsт в противном случае. При 
# передаче данных методом POST автоматиче­ски добавляется заголовок 
# Content-Type со значением application/x-www-form-urlencoded.
# Третий параметр задает максимапьное время выполнения запроса в секундах. 
# Метод воз­вращает объект класса Request.

install_opener(opener)
#

build_opener([handler, ...])
#

pathname2url(path)
#

url2pathname(path)
#

getproxies()
#


Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, 
	method=None)
#
	read(count_bites)
	# считывает данные. Если параметр не указан, возвраща­ется содержимое 
	# результата от текущей позиции указателя до конца. Если в качестве 
	# па­раметра указать число, то за каждый вызов будет возвращаться указанное 
	# количество байтов. Когда достигается конец, метод возвращает пустую 
	# строку.
	
	readline(count_bites)
	# считывает одну строку при каждом вызове. При достижении конца 
	# возвращается пустая строка. Если в необязательном параметре указа­но 
	# число, то считывание будет выполняться до тех пор, пока не встретится 
	# символ новойстроки (\n), символ конца или не будет прочитано указаююе 
	# количество байтов. Иными словами, если количество символов в строке 
	# меньше значения параметра, будет считана одна строка, а не указанное 
	# количество байтов. Если количество байтов в строке больше, возвращается 
	# указанное количество байтов.

	readlines(count_bites)
	# считывает весь результат в список. Каждый эле­мент списка будет содержать 
	# одну строку, включая символ перевода строки. Если пара­метр задан, 
	# считывается указанное количество байтов плюс фрагмент до конца строки.
	# При достижении конца возвращается nycroй список.

	__next__()
	# считывает одну строку при каждом .... вызове. При достижении конца 
	# ре­зультата возбуждается исключение StopIteration. Благодаря методу 
	# __next__() можно перебирать результат построчно с помощью цикла for. 
	# Цикл for на каждой итерации будет автоматически вызывать данный метод

	close()
	# закрывает объект результата

	geturl()
	# возвращает интернет-адрес полученного документа. Так как все 
	# перена­правления автоматически обрабатываются, интернет-адрес полученного 
	# документа мо­жет не совпадать с адресом, заданным первоначально

	info()
	# возвращает объект, с помощью которого можно получить информацию о 
	# заго­ловках ответа сервера.

	code
	# содержит код возврата в виде числа

	msg
	# содержит текстовый статус возврата

	full_url
	#

	type
	#

	host
	#

	origin_req_host
	#

	selector
	#

	data
	#

	unverifiable
	#

	method
	#

	get_method()
	#

	add_header(key, val)
	#

	add_unredirected_header(key, header)
	#

	has_header(header)
	#

	remove_header(header)
	#

	get_full_url()
	#

	set_proxy(host, type)
	#

	get_header(header_name, default=None)
	#

	header_items()
	#



OpenerDirector
# У экземпляров OpenerDirector есть следующие методы:

	add_handler(handler)
	# 
		protocol_open()
		#
		http_error_type()
		#
		protocol_error()
		#
		protocol_request()
		#
		protocol_response()
		#

	open(url, data=None[, timeout])
	#

	error(proto, *args)
	#




BaseHandler
# Объекты BaseHandler предоставляют несколько методов, которые являются 
# непосредственно полезными, и другие, которые предназначены для 
# использования производными классами.

	add_parent(director)
	# добавить дерикторию в качестве радителя

	close()
	#

	parent
	#

	default_open(req)
	#

	protocol_open(req)
	#

	unknown_open(req)
	#

	http_error_default(req, fp, code, msg, hdrs)
	#

	http_error_nnn(req, fp, code, msg, hdrs)
	#

	protocol_request(req)
	#

	protocol_response(req, response)
	#




HTTPDefaultErrorHandler
#




HTTPRedirectHandler
#
	redirect_request(req, fp, code, msg, hdrs, newurl)
	#

	http_error_301(req, fp, code, msg, hdrs)
	#

	http_error_302(req, fp, code, msg, hdrs)
	#

	http_error_303(req, fp, code, msg, hdrs)
	#

	http_error_307(req, fp, code, msg, hdrs)
	#




HTTPCookieProcessor(cookiejar=None)
#
	cookiejar
	#




ProxyHandler(proxies=None)
#
	protocol_open(request)
	#




HTTPPasswordMgr
# Эти методы доступны для объектов HTTPPasswordMgr и 
# HTTPPasswordMgrWithDefaultRealm.
 
	add_password(realm, uri, user, passwd)
	#

	find_user_password(realm, authuri)
	#




HTTPPasswordMgrWithDefaultRealm
#




HTTPPasswordMgrWithPriorAuth
# Этот диспетчер паролей расширяет HTTPPasswordMgrWithDefaultRealm для 
# поддержки URI отслеживания, для которого всегда нужно отправлять 
# учетные данные.
	add_password(realm, uri, user, passwd, is_authenticated=False)
	#

	find_user_password(realm, authuri)
	#

	update_authenticated(self, uri, is_authenticated=False)
	#

	is_authenticated(self, authuri)
	#




AbstractBasicAuthHandler(password_mgr=None)
#
	http_error_auth_reqed(authreq, host, req, headers)
	#




HTTPBasicAuthHandler(password_mgr=None)
#
	http_error_401(req, fp, code, msg, hdrs)
	#



ProxyBasicAuthHandler(password_mgr=None)
#
	http_error_407(req, fp, code, msg, hdrs)
	#



AbstractDigestAuthHandler(password_mgr=None)
# 
	http_error_auth_reqed(authreq, host, req, headers)
	#



HTTPDigestAuthHandler(password_mgr=None)
#
	http_error_401(req, fp, code, msg, hdrs)
	#



ProxyDigestAuthHandler(password_mgr=None)
#
	http_error_407(req, fp, code, msg, hdrs)
	#



HTTPHandler
# 
	http_open(req)
	#



HTTPSHandler(debuglevel=0, context=None, check_hostname=None)
#
	https_open(req)
	#



FileHandler
#
	file_open(req)
	#



DataHandler
#
	data_open(req)
	#



FTPHandler
#
	ftp_open(req)
	#



CacheFTPHandler
# Объекты CacheFTPHandler являются объектами FTPHandler со следующими 
# дополнительными методами:

	setTimeout(t)
	#

	setMaxConns(m)
	#



UnknownHandler
#
	unknown_open()
	#



HTTPErrorProcessor
#
	http_response()
	#
	
	https_response()
	#
