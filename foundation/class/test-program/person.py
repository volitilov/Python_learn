#	Person ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
from lister import ListTree

class Person(ListTree):
	'''
	Создает и обрабатывает записи с информацией о людях
	'''
	def __init__(this, name, job=None, pay=0):
		this.name = name
		this.job = job
		this.pay = pay

	def giveRaise(this, percent):
		this.pay = int(this.pay * (1 + percent))

if __name__ == '__main__':
	X = Person()
	print(X)