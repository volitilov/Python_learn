class Person:
	def __init__(this, name, job=None, pay=0):
		this.name = name
		this.job = job
		this.pay = pay

	def giveRaise(this, percent):
		this.pay = int(this.pay * (1 + percent))
	
