#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "self" ..................

#	Сделать простой пример использования self

class SuperClass:
	def sum(self, a, b):
		return a + b

class SelfTest(SuperClass):
	def __init__(self, c, x, y):
		self.c1 = dict.fromkeys([c],self.sum(x, y))
		self.c2 = dict.fromkeys([c],self.sum(9, 10))
