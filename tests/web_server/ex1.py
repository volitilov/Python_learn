#!/usr/bin/python3

# Этот простой веб-сервер может читать запросы GET, получать веб-страницу
# (файл .html) и возвращать ее вызывающему клиенту. В нем используется 
# обработчик BaseHTTPRequestHandler, который находится в модуле 
# BaseHTTPServer, и реализо­ван метод do_GET() для обработки запросов GЕТ. 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from atexit import register
from http.server import BaseHTTPRequestHandler, HTTPServer

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class My_handler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			with open(self.path[1:], 'r') as f:
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				doc = bytes(f.read(), 'utf-8')
				self.wfile.write(doc)
		except IOError:
			self.send_error(404, 'File Not Found: ' + self.path)
		


def _main():
	try:
		httpd = HTTPServer(('', 8000), My_handler)
		print('Press ^C once or twice to quit.')
		httpd.serve_forever()
		
	except KeyboardInterrupt:
		print('^C received, shutting down server')
		httpd.socket.close()



@register
def _atexit(): pass



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
