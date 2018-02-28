#!/usr/bin/python3

# небольшое тестовое задание для изучения модуля threading
# Пример: 2

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import threading
from time import sleep, ctime

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

loops = [4, 2]


class Thread_Func:
	def __init__(self, func, args, name=''):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):
		self.func(*self.args)


def loop(nloop, nsec):
	print('start loop', nloop, 'at:', ctime())
	sleep(nsec)
	print('loop', nloop, 'done at:', ctime())


def main():
	print('Starting at:', ctime())
	threads = []
	nloops = range(len(loops))

	# создаю объекты потока отдельным циклом для небольшой 
	# синхронизации начала работы потоков
	for i in nloops:
		# создаю поток в котором при запуске должна будет
		# сработать функция.
		t = threading.Thread(
			target=Thread_Func(loop, (i, loops[i]), loop.__name__))

		threads.append(t)

	for i in nloops:
		# запуск потока
		threads[i].start()

	for i in nloops:
		# ожидание завершения всех потоков
		threads[i].join()
	
	print('all DONE at:', ctime())



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	main()
