#!/usr/bin/python3

# модуль для запуска передаваемых аргументов в отдельном потоке

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import threading
from time import sleep, ctime

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class My_Thread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args

	def get_result(self):
		return self.res

	def run(self):
		print('Starting', self.name, 'at:', ctime())
		self.res = self.func(*self.args)
		print(self.name, 'finished at:', ctime())



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	print('Модуль не является сценарием, он предназначен \
	\nдля запуска передаваемых аргументов в отдельном потоке. \
	\nМодуль содержит конструктор потоков My_Thread который \
	\nпринимает функции для запуска в потоке.')

