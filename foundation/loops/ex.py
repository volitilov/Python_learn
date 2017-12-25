#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "loop" //////////////////

#	Task:

#	Программа генирации случайной строки состоящей из цифр и 
#	букв, это строка записывается объекту user и admin. Есть 
#	выбор длины строки.


def createKey(letters, complexity, testStr):

	import random

	a = list(letters)

	i = 1
	while i <= complexity:
		testStr.append(a[random.randrange(1, len(a))])
		testStr.append(str(random.randrange(0, 9)))
		i += 1 

	testStr = ''.join(testStr)
	return testStr

def recordKey(testStr, user, admin, key):
	user['testStr'] = key
	admin['testStr'] = key

	return user


#	range() ::::::::::::::::::::::::::::::::::::::::::::::::::::

for i in range(1, 6, 2):
	print(i, 'string')

#	zip() ::::::::::::::::::::::::::::::::::::::::::::::::::::::

#	ex1 ..........................
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

for (x, y) in zip(L1, L2):
	print(x, '+', y, '=', x + y)

#	ex2 ..........................
E1 = ['a', 'b', 'c'] 	# keys
E2 = [1, 2, 3] 			# values
d = {}					# dict

for (x, y) in zip(E1, E2): d[x] = y

print(
	dict(zip(E1, E2)), 
	open('test.py', 'a')
)