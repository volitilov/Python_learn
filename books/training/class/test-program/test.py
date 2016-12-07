#	person.py ::::::::::::::::::::::::::::::::::::::::::::::::

from person import Person as P

a = P('Alex')
b = P('Bob', 'developer', 1000)

b.giveRaise(.10)

print(	a.name, a.job, a.pay, '\n', # Alex None 0
		b.name, b.job, b.pay)		# Bob developer 1100

#	manager.py :::::::::::::::::::::::::::::::::::::::::::::::