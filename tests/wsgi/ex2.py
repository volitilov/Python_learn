#!/usr/bin/python3

# В этом примере перед каждой строкой результатов в приложении выводится 
# префикс в виде отметки времени.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from wsgiref.simple_server import make_server, demo_app
from time import ctime

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Ts_ci_wrap(object):
	def __init__(self, app):
		self.orig_app = app

	def __call__(self, *stuff):
		x = (x for x in self.orig_app(*stuff))
		return ('[{}] {}'.format((ctime(), x)))

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	with make_server('', 8000, Ts_ci_wrap(demo_app)) as httpd:
		print("Serving HTTP on port 8000...")
		httpd.serve_forever()
