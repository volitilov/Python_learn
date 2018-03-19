#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from atexit import register
from http.server import CGIHTTPRequestHandler
import cgitb

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def _main():
	try:
		httpd = HTTPServer(('', 8000), CGIHTTPRequestHandler)
		cgitb.enable()
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
