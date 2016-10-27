#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "dict" ////////////////

#	Task:

#	программа добавляет новую пару (ключ, значение) в словарь, 
#	но предварительно проводит проверку на число, если первая 
#	буква число то заменяет на букву, также если первая буква 
#	в строке в нижнем регистре заменяет на противоположный.


def tox(a, s):
	a = list(a);
	for i in range(len(a)):
		if a[i].isdigit():
			a[i] = s
	a[0] = a[0].upper()
	return ''.join(a)

def addKeyValue(a, b, testDict):
	testDict[tox(a,'a')] = tox(b,'b')
	return testDict