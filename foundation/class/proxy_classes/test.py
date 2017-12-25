#	ex1 ::::::::::::::::::::::::::::::::::::::::::::::

class wrapper:
	def __init__(self, object):
		self.wrapped = object	# Сохранить объект

	def __getattr__(self, attrname):
		print('Trace:', attrname) 	# Отметить факт извлечения
		return getattr(self.wrapped, attrname) 	# Делегировать извлечение

x = wrapper([1,2,3])	# Обернуть список
x.append(4) 	# Делегировать операцию методу списка
Trace: append
x.wrapped 		# [1, 2, 3, 4]

x = wrapper({“a”: 1, “b”: 2}) # Обернуть словарь
x.keys() 	# Делегировать операцию методу словаря
			# Trace: keys
			# [‘a’, ‘b’]

#	ex2 ::::::::::::::::::::::::::::::::::::::::::::::

