#	person.py ::::::::::::::::::::::::::::::::::::::::::::::::

from person import Person as P

a = P('Alex')
b = P('Bob', 'developer', 1000)

b.giveRaise(.10)

print(	a.name, a.job, a.pay, '\n', 	# Alex None 0
		b.name, b.job, b.pay, '\n',		# Bob developer 1100
		b)					# [Person: Bob, developer, 1100]

bob = P('Bob Smith')

print(  bob.__class__, '\n',	# <class 'person.Person'>
		bob.__class__.__name__, '\n', # Person
		list(bob.__dict__.keys()))	# ['job', 'pay', 'name']

for key in bob.__dict__:
	print(key, '=>', bob.__dict__[key])

	# job => None
	# name => Bob Smith
	# pay => 0

for key in bob.__dict__:
	print(key, '=>', getattr(bob, key))

	# name => Bob Smith
	# job => None
	# pay => 0

#	manager.py :::::::::::::::::::::::::::::::::::::::::::::::

from manager import Manager as M

x = M('Ali', 100)
x.giveRaise(.20)

print(x)			# [Manager: name=Ali, job=manager, pay=130]