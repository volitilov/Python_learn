# наследую класс Thread в класс MyThread и указываю, 
# чтобы его имя выводилось как stdout.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

from threading import Thread
import time, random

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

class MyThread(Thread):
	"""A threading example"""
	def __init__(self, name):
		# инициализация потока
		Thread.__init__(self)
		self.name = name

	def run(self):
		"""запуск патока"""
		amount = random.randint(2, 15)
		time.sleep(amount)
		msg = '{} is runing'.format(self.name)
		print(msg)


def create_threads():
	"""создаём группу потоков"""
	for i in range(5):
		th = MyThread('Thread #{}'.format(i+1))
		th.start()




create_threads()