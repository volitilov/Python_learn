#	ex1 ............................................

class FirstClass:
	def setdata(this, value):
		this.data = value
	def display(this):
		print(this.data)

x = FirstClass()
y = FirstClass()

x.setdata('King Tuxeus')
x.display()	# King Tuxeus

x.data = 'New value'
x.display()	# New value

x.anather = 'test'
x.anather	# test

#	ex2 ............................................

class SecondClass(FirstClass):
	def display(this):
		print('Curent value = {}'.format(this.data))

s = SecondClass()

s.setdata('test')
s.display() 	# Curent value = test

#	ex3 ............................................

class ThirdClass(SecondClass):
	def __init__(this, value):
		this.data = value
	def __add__(this, other):
		return ThirdClass(this.data + other)
	def __str__(this):
		return '[ThirdClass: {}]'.format(this.data)

a = ThirdClass('abc')
a.display() 	# Curent value = abc
print(a)		# [ThirdClass: abc]

b = a + 'dgx'
b.display()		# Curent value = abcdgx
print(b)		# [ThirdClass: abcdgx]

x = list(a.__dict__.keys())
print(x)		# [data]

# ex4 .............................................

class Person:
	def __init__(this, name, job):
		this.name = name
		this.job = job
	def info(this):
		return (this.name, this.job)

z1 = Person('Aleks', 'developer')
z2 = Person('Bob', 'streat-cleaner')

print(z1.name, '=>', z1.job)
print(z2.name, '=>', z2.job)