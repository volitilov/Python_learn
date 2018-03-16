requests ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Этот модуль упращает загрузку файлов из интернета, позволяя не 
# задумываться о таких сложных вопросах, как ошибки сети, проблемы 
# подключения сжатия данных

# документация на английском:
# http://docs.python-requests.org/en/master/
# http://docs.python-requests.org/en/master/api/

# установка:
pip install requests

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import requests as r

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
r.requests(method, url, **kwargs)
# конструктор запросов
	method
	# метод для HTTP запроса
	url
	# адрес запроса
	params
	# объект запроса в виде словоря или бинарных данных
	data
	# словарь или список кортежей [(key, value)] который будет 
	# закодирован в байты или файло-подобный объект для передачи 
	# вместе с запросом
	json
	# json данные которые будут отправлены в теле запроса
	headers
	# словарь HTTP заголовка отправленный вместе с запросом
	cookies
	# отправка кукисов в виде словаря или CookieJar
	files
	# отправка словаря с 'name': file-like-objects (или 
	# {'name': file-tuple}) для многострочной закодированной 
	# загрузки. file-tuple может быть: 
	# 2-кортежным ('filename', fileobj), 
	# 3-кортежным ('filename', fileobj, 'content_type'),
	# 4-кортежным ('filename', fileobj, 'content_type', custom_headers), 
	# где «content-type» - это строка, определяющая тип 
	# содержимого данного файла, а custom_headers - объект типа dict, 
	# содержащий дополнительные заголовки для добавления файла. 
	auth
	# кортеж авторизации содержащий (login, password) для включения 
	# Basic/Digest/Custom HTTP Auth (другими словами базовая 
	# авторизация)
	timeout
	# устанавливает время на установление запроса и чтения. 
	# Можно либо float сразу на всё, 
	# либо typle(connect timeout, read timeout)
	allow_redirects
	# Boolean. Включить/отключить 
	# GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD перенаправление. 
	# По умолчанию используется значение True.
	proxies
	# Протокол сопоставления словаря с URL-адресом прокси-сервера.
	verify
	# Boolen, контролирует проверку сертификата TLS сервера, 
	# или строку, и в данном случае дулжен быть указан путь к 
	# CA bundle. По умалчанию значение True.
	stream
	# если False, содержимое ответа будет немедленно загружено
	cert
	# если строка то указывается, путь к файлу сертификата клиента 
	# ssl(.pem). Если кортеж то, ('cert', 'key') пара.


r.post(url, data={'key':'value'})
r.put(url, data={'key':'value'})
r.delete(url)
r.head(url)
r.options(url)
# делаем запросы соответствующих типов




# response object ::::::::::::::::::::::::::::::::::::::::::::::::: 

res = r.get(url)
# принимает строку с url-адресом по которому должна 
# осуществляться загрузка

res.status_code
# код статуса

res.text
# в случае успешного выполнения запроса загруженная страница
# сохраняется в виде строки в переменной text

res.headers['content-type']
# получение значения content-type в заголовке

res.encoding
# в какой кодировке ответ

res.json()
# получения ответа в формате json

res.url
# url ответа

res.raw
# получение объекта сокета

res.raise_for_status()
# возбуждает исключение, если в процессе обработки запроса 
# произашла ошибка, и не совершает не каких действий в случае
# успешной загрузки

res.iter_content(100000)
# возвращает порции содердимого на каждой стадии цикла.
# Каждая порция данных - это данные байтового типа, можно 
# указать сколько байтов должна содержать каждая порция

res.cookies['ex_cookie_name']
# если ответ содержит cookies, то таким образом можно их получить

res.history
# можно использовать свойство history объекта Response для 
# отслеживания перенаправления, при условии что allow_redirects
# включено в True при отправке запроса




# request Sessions ::::::::::::::::::::::::::::::::::::::::::::::::

s = r.Sessions()
# создаёт и открывает объект для работы с сесией

s.close()
# закрытие сессии

s.cookies
# CookieJar объект, содержащий все имеющиеся в настоящее время 
# файлы cookie, установленные на этом сеансе. По умолчанию это 
# RequestsCookieJar, но может быть любым другим совместимым с 
# cookielib.CookieJar объектом.

s.get(url)
s.delete(url, **kwargs)
s.head(url, **kwargs)
# и т.д как в обычном запросе

s.get_adapter(url)
# Возвращает соответствующий адаптер подключения для данного 
# URL-адреса.

get_redirect_target(resp)
# вернёт URI перенаправления

headers = None
# получение заголовков запроса

hooks = None
# включение/отключение перехватчиков событий

max_redirects = None
# Максимальное количество разрешенных перенаправлений. Если запрос 
# превышает этот предел, возникает исключение TooManyRedirects. 
# По умолчанию используется requests.models.DEFAULT_REDIRECT_LIMIT, 
# который равен 30.

merge_environment_settings(url, proxies, stream, verify, cert)
# проверяет среду и объеденияет её с некоторыми настройками.

mount(prefix, adapter)
# Регистрирует адаптер подключения к префиксу. Адаптеры сортируются 
# в порядке убывания по длине префикса.

patch(url, data=None, **kwargs)
# отправляет запрос patch

prepare_request(request)
# Создает PreparedRequest для передачи и возвращает его. 
# PreparedRequest имеет настройки, объединенные с экземпляром 
# запроса и сеансами.
	request
	# экземпляр запроса

rebuild_auth(prepared_request, response)
# При перенаправлении мы можем удалить аутентификацию из запроса, 
# чтобы избежать утечки учетных данных. Этот метод интеллектуально 
# удаляет и повторно использует аутентификацию, где это возможно, 
# чтобы избежать потери учетных данных.

rebuild_method(prepared_request, response)
# При перенаправлении мы можем захотеть изменить метод запроса на 
# основе определенных спецификаций или поведения браузера.

rebuild_proxies(prepared_request, proxies)
# Этот метод переоценивает конфигурацию прокси, рассматривая 
# переменные среды. Если мы перенаправлены на URL-адрес, 
# охватываемый NO_PROXY, мы удалим конфигурацию прокси-сервера. 
# В противном случае мы устанавливаем отсутствующие ключи прокси 
# для этого URL (в случае, если они были удалены предыдущим 
# перенаправлением). Этот метод также заменяет заголовок 
# прокси-авторизации, где это необходимо.

resolve_redirects(resp, req, stream=False, timeout=None, 
	verify=True, cert=None, proxies=None, yield_requests=False, 
	**adapter_kwargs)
# Получает ответ. Возвращает генератор ответов или запросов.

send(request, **kwargs)
# отправить PreparedRequest

trust_env = None
# Настройки среды доверия для конфигурации прокси.

verify = None
# Проверка SSL по умолчанию.



# Lower-Level Classes :::::::::::::::::::::::::::::::::::::::::::::
class r.Request(method=None, url=None, headers=None, files=None, 
	data=None, params=None, auth=None, cookies=None, 
	hooks=None, json=None)
# пользовательский объект запроса

deregister_hook(event, hook)
# Отмените регистрацию зарегистрированного ранее hook. Возвращает 
# True, если hook существует, False, если нет.

prepare()
# Создает PreparedRequest для передачи и возвращает его.

register_hook(event, hook)
# правильно зарегестрирует hook

# |||||||||||||||||||||||||||||||||||||

class r.Response
# Объект Response, который содержит ответ сервера на HTTP-запрос

apparent_encoding
# Очевидная кодировка, предоставляемая библиотекой шрифтов.

close()
# Как только этот метод был вызван, базовый необработанный объект 
# не должен быть снова доступен.

content
# контент ответа сервера в байтах

cookies = None
# кукисы которые вернул сервер

elapsed = None
# Количество времени, прошедшего между отправкой запроса и 
# прибытием ответа (как timedelta). Это свойство конкретно измеряет 
# время, затрачиваемое на отправку первого байта запроса и 
# завершение анализа заголовков.

encoding = None
# Кодирование для декодирования при доступе к r.text

is_permanent_redirect
# True, если этот ответ является одной из постоянных версий 
# перенаправления.

is_redirect
# True, если этот ответ является хорошо сформированной 
# переадресацией HTTP, которая могла быть обработана автоматически 
# (через Session.resolve_redirects).

iter_content(chunk_size=1, decode_unicode=False)
# возвращает порции содердимого на каждой стадии цикла.
# Каждая порция данных - это данные байтового типа, можно 
# указать сколько байтов должна содержать каждая порция

iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)
# Итерации по данным ответа, по одной строке за раз. Когда в запросе 
# задано stream = True, это позволяет избежать одновременного чтения 
# содержимого в памяти для больших ответов.



# Authentication :::::::::::::::::::::::::::::::::::::::::::::::::::
from requests.auth import *
# Этот модуль содержит обработчики проверки подлинности для запросов.

class AuthBase
# базовый класс для авторизации

class HTTPBasicAuth(username, password)
# Подключает базовую аутентификацию HTTP к данному объекту Request.

class HTTPProxyAuth(username, password)
# Присоединяет аутентификацию HTTP-прокси к заданному объекту Request

class HTTPDigestAuth(username, password)
# Прикрепляет аутентификацию HTTP Digest к данному объекту Request.




# Cookies ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
from requests.utils import dict_from_cookiejar, add_dict_to_cookiejar
from requests.cookies import *

dict_from_cookiejar(cj)
# Возвращает словарь для запрошенного CookieJar объекта

add_dict_to_cookiejar(cj, cookie_dict)
# вставляет кукисы в указаный словарь

cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
# возвращает CookieJar из словоря 
	cookie_dict
	# словарь ключ/значение для вставки в CookieJar
	cookiejar
	#  Cookiejar для добавления файлов cookie.
	overwrite
	# Если False, не будет заменять файлы cookie уже в jar новыми.

add_cookie_header(request)
# 

clear(domain=None, path=None, name=None)
# очищает некоторые файлы cookie

clear_expired_cookies()
# очистеть все истёкшие файлы cookie

clear_session_cookies()
# очистить все сеансовые файлы cookie

copy()
# вернёт копию RequestsCookieJar.

extract_cookies(response, request)
# Извлеките файлы cookie из ответа, где это разрешено с учетом 
# запроса.

get(name, default=None, domain=None, path=None)
# 

get_dict(domain=None, path=None)
# Принимает в качестве аргумента дополнительный домен и путь и 
# возвращает простой Python словарь пар имен-значений куки-файлов, 
# соответствующих требованиям.





# exceptions :::::::::::::::::::::::::::::::::::::::::::::::::::::::

r.RequestException(*args, **kwargs)
# при обработке запроса произошла неоднозначная ошибка

r.ConnectionError(*args, **kwargs)
# ошибка подключения

r.HTTPError(*args, **kwargs)
# произошла ошибка HTTP

r.URLRequired(*args, **kwargs)
# недействительный URL

r.TooManyRedirects(*args, **kwargs)
# слишком много перенаправлений

r.ConnectTimeout(*args, **kwargs)
# вышло время при попытке подключиться к удалённому серверу

r.ReadTimeout(*args, **kwargs)
# сервер не отправляет не каких данных за выделеный промежуток
# времени

r.Timeout(*args, **kwargs)
# время запроса вышло
