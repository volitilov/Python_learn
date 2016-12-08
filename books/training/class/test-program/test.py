#	person.py ::::::::::::::::::::::::::::::::::::::::::::::::

from person import Person as P

a = P('Alex')
b = P('Bob', 'developer', 1000)

b.giveRaise(.10)

print(	a.name, a.job, a.pay, '\n', 	# Alex None 0
		b.name, b.job, b.pay, '\n',		# Bob developer 1100
		b)								# [Person: Bob, developer, 1100]

#	manager.py :::::::::::::::::::::::::::::::::::::::::::::::

from manager import Manager as M

x = M('Ali', 'blumen', 100)
x.giveRaise(.20)

print(x)								# [Person: Ali, blumen, 130]