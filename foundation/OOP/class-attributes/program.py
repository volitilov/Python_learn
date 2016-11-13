#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "class-attributes" ......

#	Task:

#	Написать простой класс конструктор который уже имеет 
#	внутри набор атрибутов и методов	

class Simple:
	'''Простой класс'''

	test = "hello world"

	def testFunction(self, a, b): 
		return a + b

	def __init__(self, random, summ):
		self.r = random.randrange(0, 55, 2)
		self.s = summ + 1
