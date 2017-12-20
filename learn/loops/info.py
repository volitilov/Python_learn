#	while ::::::::::::::::::::::::::::::::::::::::::::::::::::

while True:
	reply = input('Hellow, your name? ')
	if reply == 'stop': break
	print('Good name:', reply.upper())
	if reply == 'next': continue

#	for ::::::::::::::::::::::::::::::::::::::::::::::::::::::

#	применение к строкам .....................................

x = 'test'
for c in x: print(c, end=' ')

#	применение к картежам ....................................

x2 = ('zaza', '123', x)
for c in x2: print(c, end=', ')

#	применение к спискам .....................................

x3 = [(1, 2), (3, 4), (5, 6)]
for (a, b) in x3:
	print(a, b)

#	применение к словарям ....................................

x4 = {'a': 1, 'b': 2, 'c': 3}

for key in x4:
	print(key, '=>', x4[key])

#	обход ключей и значений одновременно
for (key, value) in x4.items():
	print(key, '=>', value)

#	применгение к файлам ....................................

for lalka in open('test.py').readline():
	print(lalka, end='')
