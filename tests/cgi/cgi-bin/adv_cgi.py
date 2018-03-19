#!/usr/bin/python3

# В этом сценарии содержится один основной класс AdvCGI, имеющий 
# немно­го более широкое назначение. В нем представлены методы, 
# предназначенные для отображения страниц с формой, сообщением об ошибке 
# или результатами, а также методы чтения или записи сооkiе-файлов на 
# клиентском компьютере (где развернут веб-браузер).

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from cgi import FieldStorage
from os import environ
from io import StringIO
from urllib.parse import quote, unquote

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class AdvCGI(object):
	header = 'Content-Type: text/html\n\n'
	url = '/cgi-bin/adv_cgi.py'
	form_html = '''
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset="utf-8">
				<title>Friends CGI title</title>
			</head>
			<body>
				<h2>Advanced CGI Demo Form</h2>
				<form method="POST" action="{}" enctype="multipart/form-data">
					<h3>My Cookie Setting</h3>
					<li><code><b>CPPuser = {}</b></code></li>
					<h3>
						Enter cookie value
						<br>
						<input name="cookie" value="{}">
						(<i>optional</i>)
					</h3>
					<h3>
						What languages can you program in?
						(<i>at least one required</i>)
					</h3>
					<h3>
						Enter file to upload
						<small>(max size 4k)</small>
					</h3>
					<input type="file" name="upfile" value="{}" size=45>
					<br>
					<input type="submit">
				</form>
			</body>
		</html>
	'''

	lang_set = ('Python', 'Ruby', 'Java', 'C++', 'PHP', 'C', 'JavaScript')
	lang_item = '<input type="checkbox" name="lang" value="{}" {}> {}\n'


	# считываю cookie файлы у клиента
	def get_CPP_Cookies(self):
		if 'HTTP_COOKIE' in environ:
			cookies = [x.strip() for x in environ['HTTP_COOKIE'].split(';')]
			for each_cookie in cookies:
				if len(each_cookie) > 6 and each_cookie[:3] == 'CPP':
					tag = each_cookie[3:7]
					try:
						self.cookies[tag] = eval(unquote(each_cookie[8:]))
					except (NameError, SyntaxError):
						self.cookies[tag] = unquote(each_cookie[8:])
			
			if 'info' not in self.cookies:
				self.cookies['info'] = ''

			if 'user' not in self.cookies:
				self.cookies['user'] = ''
		else:
			self.cookies['info'] = self.cookies['user'] = ''

		if self.cookies['info'] != '':
			self.who, lang_str, self.fn = self.cookies['info'].split(':')
			self.langs = lang_str.split(',')
		else:
			self.who = self.fn = ' '
			self.langs = ['Python']


	def show_form(self):
		self.get_CPP_Cookies()

		# объеденяю флажки выбора языка
		lang_str = []

		for each_lang in AdvCGI.lang_set:
			lang_str.append(AdvCGI.lang_item.format(each_lang, 
				('checked' if each_lang in self.langs else ''), 
				each_lang))

		# проверяю, установлены ли ещё cookie-файлы пользователя
		if not ('user' in self.cookies['user']):
			cook_status = '<i>(cookies has not been set yet)</i>'
			user_cook = ''
		else:
			user_cook = cook_status = self.cookies['user']

		print('{}{}'.format(AdvCGI.header, 
			AdvCGI.form_html.format(AdvCGI.url, cook_status,
				user_cook, self.who, 
				''.join(lang_str), self.fn)))


	err_html = '''
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset="utf-8">
				<title>Friends CGI title</title>
			</head>
			<body>
				<h3>ERROR</h3>
				<b>{}</b>
				<br>
				<form>
					<input type="button" value=Back onclick="window.history.back()">
				</form>
			</body>
		</html>
	'''

	def show_error(self):
		print(AdvCGI.header + AdvCGI.err_html.format(self.error))


	res_html = '''
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset="utf-8">
				<title>Friends CGI title</title>
			</head>
			<body>
				<h2>Your Uploaded Data</h2>
				<h3>Your cookie value is: <b>{}</b></h3>
				<h3>Your name is: <b>{}</b></h3>
				<h3>You can program in the following languages:</h3>
				<ul>{}</ul>
				<h3>
					Your Uploaded file...
					<br>Name: <i>{}</i>
					<br>Contents:
				</h3>
				<pre>{}</pre>
				<p>Click <a href="{}"><b>here</b></a> to return to form.</p>
			</body>
		</html>
	'''

	# просим клиента сохранить cookie-файлы
	def set_CPP_cookies(self):
		for each_cookie in self.cookies.keys():
			print('Set-Cookie: CPP{}={}; path=/'.format(each_cookie, 
				quote(self.cookies[each_cookie])))


	# вывожу итоговую страницу
	def do_results(self):
		MAXBYTES = 4096
		res = (each_lang for each_lang in self.langs)
		lang_list = ''.join('<li>{}<br></li>'.format(res))
		file_data = self.fp.read(MAXBYTES)
		if len(file_data) == MAXBYTES and f.read():
			file_data = '{}{}'.format(file_data, 
				'...<b><i>(file truncated due to size)</i></b>')

		self.fp.close()
		if file_data == '':
			file_data = '<b><i>(file not given or upload error)</i></b>'

		filename = self.fn

		# проверяю, установлены ли ещё cookie-файлы пользователя
		if not ('user' in slef.cookies and self.cookies['user']):
			cook_status = '<i>(cookie has not been set yet)</i>' 
			user_cook = ''
		else:
			user_cook = cook_status = self.cookies['user']

		# устанавливаю cookie-файлы
		self.cookies['info'] = ':'.join(
			(self.who, ','.join(self.langs, ','), filename))
		self.set_CPP_cookies()

		print('{}{}'.format(AdvCGI.header, AdvCGI.res_html.format(
			cook_status, self.who, lang_list, filename, 
			file_data, AdvCGI.url)))


	# определяю какую страницу вернуть
	def go(self):
		self.cookies = {}
		self.error = ''
		form  = FieldStorage()
		if not form.keys():
			self.show_form()
			return

		if 'person' in form:
			self.who = form['person'].value.strip().title()
			if self.who == '':
				self.error = 'Your name is required. (blank)'
			else:
				self.error = 'Your name is required. (missing)'

		self.cookies['user'] = unquote(form['cookie'].value.strip()) if 'cookie' in form else ''

		if 'lang' in form:
			lang_data = form['lang']
			if isinstance(lang_data, list):
				self.langs = [each_lang.value for each_lang in lang_data]
			else:
				self.langs = [lang_data.value]
		else:
			self.error = 'At least one language required.'

		if 'upfile' in form:
			upfile = form['upfile']
			self.fn = upfile.filename or ''
			if upfile.file:
				self.fp = upfile.file
			else:
				self.fp = StringIO('(no data)')
		else:
			self.fp = StringIO('(no file)')
			self.fn = ''


		if not self.error:
			self.do_results()
		else:
			self.show_error()




# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	page = AdvCGI()
	page.go()
