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
