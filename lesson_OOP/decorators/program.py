#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "decorators" ............

#	Task:

#	Пример использования дикоратора.

#	example 1:...............................................
def a(this):
	def b(arg1, arg2):
		print('test')
		this(arg1, arg2)
		print('test2')
	return b

@a
def c(a, b):
	print(a + b)

#	example 2:...............................................
def logging(this):
	def wrapper(*args, **kwargs):
		res = this(*args, **kwargs)
		print(this.__name__, args, kwargs)
		return res
	return wrapper

def test(this):
	def wrap(self):
		print('Я Вячеслав Волитилов')
		this(self)
		print('У меня всё good.')
	return wrap

@logging
class Ex:
	def __init__(self, a):
		self.age = 26
		self.a = a
		self.zaza()
	@test
	def zaza(self):
		print('Мне {} лет.'.format(self.age + self.a))
