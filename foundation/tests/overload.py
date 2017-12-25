# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Number:
	def __init__(self, start):
		self.data = start
	def __sub__(self, other):
		return Number(self.data - other)

t = Number(5)
t2 = t - 3
# print(t2.data) # 2

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Indexer:
	def __getitem__(self, index):
		return index ** 2

z = Indexer()
# print(z[3])		# 9

for i in range(10):
	print(z[i], end=' ')

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Squares:
	def gsquares(self, start, stop):
		for i in range(start, stop + 1):
			yield i ** 2

B = Squares()

for c in B.gsquares(1, 5):
	print(c, end=' ')

# или: (x ** 2 for x in range(1, 5))

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Adder:
	def __init__(self, value=0):
		self.data = value
	def __add__(self, other):
		self.data += other

x = Adder()
# print(x)	# <__main__.Adder object at 0x7f490f3a0898>

class Addrepr(Adder):
	def __repr__(self):
		return 'self.data + other = {}'.format(self.data)

x = Addrepr(2)
x + 1
# print(x)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Addboth(Adder):
	def __str__(self):
		return '[Value: {}]'.format(self.data)
	def __repr__(self):
		return 'self.data + other = {}'.format(self.data)

y = Addboth(3)
y + 1
y 	# использует method.__repr__ для вывода в интер. режиме
# print(y) # использует method.__str__
str(y) # использует method.__str__ для вывода в интер. режиме
repr(y) # использует method.__repr__ для вывода в интер. режиме

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Callee:
	def __call__(self, *pargs, **kargs):
		print('Called: {}, {}'.format(pargs, kargs))

x = Callee()
x(1, 2, 3) # Called: (1, 2, 3), {}
x(1, 2, a=3, b=4) # Caleed: (1, 2), {'a': 3, 'b': 4}

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Prod:
	def __init__(self, value):
		self.value = value
	def __call__(self, other):
		return self.value * other

y = Prod(2)
print(y(3)) # 6