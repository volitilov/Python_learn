#!/usr/bin/python3

# упрощенная модель ав­томата для торговли конфетами. В данном 
# конкретном автомате имеются в наличии только пять карманов, 
# заполняемых запасом товара (шоколадными батончиками).
# Если заполнены все карманы, то в автомат больше нельзя заправить 
# ни одной кон­феты и, аналогично, при отсутствии в автомате 
# шоколадных батончиков какого-то конкретного типа покупатели, 
# желающие приобрести именно их, будут вынуждены возвратиться с 
# пустыми руками. В данном случае ресурсы (карманы для конфет) 
# яв­ляются конечными, и для отслеживания их состояния будет 
# использован семафор. 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import ctime, sleep

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

lock = Lock()
# кол-во конфет
MAX = 5
# автомат с запасами
candytray = BoundedSemaphore(MAX)


# пополнение запасов автомата, увеличев товар на 1, если автомат 
# полон, симофор выкенет ValueError.
def refill():
	lock.acquire()
	print('Пополнение автомата...')
	try:
		candytray.release()
	except ValueError:
		print('...автомат поный')
	else:
		print('OK')
	lock.release()


# покупка товара из автомата, уменьшая товар на 1, если автомат
# пуст напишет 'empty, scipping'
def buy():
	lock.acquire()
	print('Покупка конфет...', )
	if candytray.acquire(False):
		print('OK')
	else:
		print('атомат пуст')
	lock.release()


# моделирует поведение пополнения автомата товаром
def producer(loops):
	for i in range(loops):
		refill()
		sleep(randrange(3))


# моделирует поведение потребления товара
def consumer(loops):
	for i in range(loops):
		buy()
		sleep(randrange(3))

# 
def _main():
	print('начало в:', ctime())
	nloops = randrange(2, 6)
	print('АВТОМАТ С КОНФЕТАМИ (в наличии {})!'.format(MAX))
	Thread(
		target=consumer, 
		args=(randrange(nloops, nloops+MAX+2),)
	).start()
	Thread(target=producer, args=(nloops,)).start()



@register
def _atexit():
	print('программа завершена в:', ctime())


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
