#	ex1 ::::::::::::::::::::::::::::::::::::::::::::::::::

y = 1

def y1():
	print(y)

def y2():
	y = 2
	print(y)

class Y3():
	y = 3
	def y3(self):
		y = 4
		self.y = 5


#	ex2 ::::::::::::::::::::::::::::::::::::::::::::::::::

x = 1

def x1():
	print(x)

def x2():
	global x
	x = 2

def x3():
	x = 3
	def x3_1():
		print(x)

def x4():
	x = 4
	def x4_1():
		nonlocal x
		x = 5

#	ex3 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Test: pass

class Super:
	def hay(self):
		self.data1 = 'test => Super.method'

xx = Super()
# print(xx.__class__)
xx.hay()
# print(xx.data1)
# print(xx.__dict__)
# print(list(xx.__dict__.keys()))

class Sub(Super, Test):
	def hello(self):
		self.data2 = 'test => Sub.method'

# print(Sub.__bases__)
yy = Sub()
yy.hay()
yy.hello()
# print(yy.data1, '\n', yy.data2)
# print(yy.__dict__)
# print(sorted(list(yy.__dict__.keys())))

#	ex4 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Number:
	def __init__(self, start):
		self.data = start
	def __sub__(self, other):
		return Number(self.data - other)

t = Number(5)
t2 = t - 3
# print(t2.data) # 2

#	ex5 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Indexer:
	def __getitem__(self, index):
		return index ** 2

z = Indexer()
# print(z[3])		# 9

# for i in range(10):
# 	print(z[i], end=' ')

#	ex6 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Squares:
	def gsquares(self, start, stop):
		for i in range(start, stop + 1):
			yield i ** 2

B = Squares()

for c in B.gsquares(1, 5):
	print(c, end=' ')

# или: (x ** 2 for x in range(1, 5))

#	ex7 ::::::::::::::::::::::::::::::::::::::::::::::::::

