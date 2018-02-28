#!/usr/bin/python3

# В этом примере демонстрируется использование блокировок и 
# других инструмен­тов обеспечения многопоточного функционирования.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from atexit import register
from random import randrange
from threading import Thread, current_thread, Lock
from time import sleep, ctime

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# создаю подклас множества для переопределения операции вывода
class Clean_output_set(set):
	def __str__(self):
		return ', '.join(x for x in self)



lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = Clean_output_set()



# Функция loop() сохраняет имя текущеrо потока, в котором она 
# выполняется, за­тем захватывает блокировку, что позволяет сделать 
# неразрывным (атомарным) сле­дующий ряд операций: добавление имени 
# к множеству remaining и формирование вывода с указанием на начало 
# потока (с этого момента больше никакой другой поток не сможет 
# войти в критический участок кода). После освобождения блокировки 
# этот поток приостанавливается на время в секундах, выбранное 
# случайным образом, затем повторно захватывает блокировку, чтобы 
# сформировать свой окончательный вывод перед ее освобождением.
def loop(nsec):
	my_name = current_thread().name
	with lock:
		remaining.add(my_name)
		print(ctime(), 'Started', my_name)
	
	sleep(nsec)
	
	with lock:
		remaining.remove(my_name)
		print(ctime(), 'Completed', my_name, nsec)
		print('	remaining:', (remaining or 'None'))



def _main():
	for pause in loops:
		Thread(target=loop, args=(pause,)).start()


# функция которую вызывает интерпретатор непосредственно перед 
# завершением сцинария. 
@register
def _atexit():
	print('all Done at:', ctime())




# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
