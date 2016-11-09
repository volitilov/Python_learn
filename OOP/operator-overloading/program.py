#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "operator overloading" ..

#	Простой пример переопределения метода класса:
#	Есть класс который возвращает сумму двух чисел, задача
#	заключается в том чтобы переопределить сложение на 
#	вычетание.

class Overloading:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		self.count()

	def count(self):
		self.c = self.a + self.b


class Redefinition(Overloading):
	def count(self):
		self.c = self.a - self.b