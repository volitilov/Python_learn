#!/usr/bin/python3

# небольшое тестовое задание для изучения модуля threading
# Пример: 3

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import threading
from time import sleep, ctime

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

loops = [4, 2]


class My_Thread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args

	def run(self):
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
		t = My_Thread(loop, (i, loops[i]), loop.__name__)

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
