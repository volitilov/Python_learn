#!/usr/bin/python3

# небольшое тестовое задание для изучения модуля _thread

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import _thread
from time import sleep, ctime

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

loops = [4, 2]

def loop(nloop, nsec, lock):
	print('start loop', nloop, 'at:', ctime())
	sleep(nsec)
	print('loop', nloop, 'done at:', ctime())
	# освобождаю блокировку
	lock.release()

def main():
	print('Starting at:', ctime())
	locks = []
	nloops = range(len(loops))

	for i in nloops:
		# создаю объект блокировки в разблокированном состоянии
		lock = _thread.allocate_lock()
		# захватываю объект блокировки
		lock.acquire()

		locks.append(lock)

	for i in nloops:
		# запускаю функцию в потоке, которая засыпает на указанное
		# время, и отключает блокировку, когда она завершит свою
		# работу
		_thread.start_new_thread(loop, (i, loops[i], locks[i]))

	for i in nloops:
		# Цикл будет продалжяться пока функции не закончат свою
		# работу и не отключат блокировку.
		while locks[i].locked(): pass
	
	print('all DONE at:', ctime())



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	main()
