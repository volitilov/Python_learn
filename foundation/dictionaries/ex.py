d = {} 			# создаём словарь с помощью литерала

d = dict() 		# создание словаря с помошью метода dict()

d = dict.fromkeys(['a', 'b'], 100)   # с помощью метода fromkeys()
d 	# {'a': 100, 'b': 100}

x = {a: a ** 2 for a in range(7)} 	# создание с помощью генератора
x	 # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel		# {'sape': 4139, 'guido': 4127, 'jack': 4098}
tel['jack'] 	# 4098	
del tel['sape']
tel['irv'] = 4127
tel		# {'guido': 4127, 'irv': 4127, 'jack': 4098}

lol = [['a', 1], ['b', 2], ['c', 3]]
dict(lol) # {'b': 2, 'a': 1, 'c': 3}

lot = [('a', 1), ('b', 2), ('c', 3)]
dict(lot) # {'b': 2, 'a': 1, 'c': 3}

tol = (['a', 1], ['b', 2])
dict(tol) # {'b': 2, 'a': 1}

los = ['ab', 'cd']
dict(los) # {'a': 'b', 'c': 'd'}

tos = ('ab', 'cd')
dict(tos) # {'a': 'b', 'c': 'd'}