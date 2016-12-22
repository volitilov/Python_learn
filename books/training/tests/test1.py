#	ex1 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Ex1:
	z = 'lsk'
	def x(self, value):
		self.data = value
	def y(self):
		print(self.data)

# ekz = Ex1()
# ekz.x('xxx')
# print(ekz.data) # xxx
# ekz.y()			# xxx

# ekz.data = '---'
# ekz.newatr = 'www'
# print(ekz.data) # ---
# print(ekz.newatr) # www

# print(Ex1.z) 	# 'lsk'

#	ex2 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Ex2(Ex1):
	def y(self):
		print('New value: {}'.format(self.data))

# qqq = Ex2()
# qqq.x('zzz')
# print(qqq.data) # zzz
# qqq.y() 	# New value: zzz

#	ex3 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Ex3(Ex2):
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return Ex3(self.data + other)
	def __str__(self):
		return '[Ex3: {}]'.format(self.data)
	def test(self, other):
		self.data *= other

a = Ex3('abc')
a.y() 	# New value: abc
print(a) # [Ex3: abc]

b = '-ghy-'
c = a + b	# Новый __add__: создается новый экземпляр
c.y() 	# New value: abc-ghy-
print(c) # [Ex3: abc-ghy-]

a.test(2)
print(a) # [Ex3: abcabc]
c.test(3)
print(c) # [Ex3: abc-ghy-abc-ghy-abc-ghy-]

