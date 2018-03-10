#!/usr/bin/python3

# В этой реализации принципа "производитель-потребитель" 
# используются объек­ты Queue и вырабатывается случайным образом 
# количество произведенных (и потре­бленных) товаров. Производитель 
# и потребитель моделируются с помощью потоков, действующих 
# отдельно и одновременно. 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from random import randint
from time import sleep
from queue import Queue
from cr_thread import My_Thread

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# помещает объект в очередь
def write_q(queue):
	queue.put('xxx', 1)
	print('producing object for Q... size now', queue.qsize())


# забирает объект из очереди
def read_q(queue):
	val = queue.get(1)
	print('consumed object from Q... size now', queue.qsize())


# выполняется как отдельный поток, единственным назначением 
# которого является выработка одного элемента для постановки 
# в очередь, переход на время в состояние ожидания, а затем 
# повтор этого цикла указанное количество раз, причем 
# количество повторов устанавливается при выполнении сценария 
# случайным образом.
def writer(queue, loops):
	for i in range(loops):
		write_q(queue)
		sleep(randint(1, 3))


# действует аналогично методу writer(), если не считать того, 
# что он не ста­вит, а извлекает элементы из очереди
def reader(queue, loops):
	for i in range(loops):
		read_q(queue)
		sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


# Соз­даются необходимые потоки и осуществляется их запуск, а 
# окончание работы насту­пает после того, как оба потока завершают 
# свое выполнение.
def _main():
	nloops = randint(2, 5)
	q = Queue(32)

	threads = []
	for i in nfuncs:
		t = My_Thread(funcs[i], (q, nloops), funcs[i].__name__)
		threads.append(t)

	for i in nfuncs:
		threads[i].start()

	for i in nfuncs:
		threads[i].join()
	

	print('all DONE')
	



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
