#	/////////////////////////////////////////////////////////////
#	Пперезагрузка операторов.....................................

# 	Перегрузка операторов — один из способов реализации полиморфизма,
# 	когда мы можем задать свою реализацию какого-либо метода в своём 
#	классе.

#	Например, у нас есть два класса:

	class A:
    	def go(self):
        	print('Go, A!')

	class B(A):
    	def go(self, name):
        	print('Go, {}!'.format(name))

#	В данном примере класс B наследует класс A, но переопределяет 
#	метод go, поэтому он имеет мало общего с аналогичным методом 
#	класса A.

#	Однако в python имеются методы, которые, как правило, не 
#	вызываются напрямую, а вызываются встроенными функциями или 
#	операторами.

#	Например, метод __init__ перегружает конструктор класса. 
#	Конструктор - создание экземпляра класса.

	class A:
		def __init__(self, name):
			self.name = name

	a = A('Vasya')
	print(a.name) 	# Vasya

#	Список таких "магических" методов  можно посмотреть в
#	папке _useful-library_ файл class_methods.py.

#	Рассмотрим некоторые из этих методов на примере двухмерного 
#	вектора, для которого переопределим некоторые методы:

	import math

	class Vector2D:
    	def __init__(self, x, y):
        	self.x = x
        	self.y = y

    	def __repr__(self):
        	return 'Vector2D({}, {})'.format(self.x, self.y)

    	def __str__(self):
        	return '({}, {})'.format(self.x, self.y)

    	def __add__(self, other):
        	return Vector2D(self.x + other.x, self.y + other.y)

    	def __iadd__(self, other):
        	self.x += other.x
        	self.y += other.y
        	return self

    	def __sub__(self, other):
        	return Vector2D(self.x - other.x, self.y - other.y)

    	def __isub__(self, other):
        	self.x -= other.x
        	self.y -= other.y
        	return self

    	def __abs__(self):
        	return math.hypot(self.x, self.y)

    	def __bool__(self):
        	return self.x != 0 or self.y != 0

    	def __neg__(self):
        	return Vector2D(-self.x, -self.y)

	x = Vector2D(3, 4)
	x 	# Vector2D(3, 4)
	print(x) 	# (3, 4)
	abs(x) 	# 5.0
	y = Vector2D(5, 6)
	y 	# Vector2D(5, 6)
	x + y	# Vector2D(8, 10)
	x - y 	# Vector2D(-2, -2)
	-x 	# Vector2D(-3, -4)
	x += y
	x 	# Vector2D(8, 10)
	bool(x) # True
	z = Vector2D(0, 0)
	bool(z) # False
	-z 	# Vector2D(0, 0)

# 	В заключение хочу сказать, что перегрузка специальных методов - вещь 
# 	хорошая, но не стоит ей слишком злоупотреблять. Перегружайте их только 
# 	тогда, когда вы уверены в том, что это поможет пониманию программного 
#	кода.