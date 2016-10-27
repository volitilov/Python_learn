#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "множества" ////////////////

#	Task:

#	Сделать программу которая будет искать переданные параметры 
#	в множестве, если не находит, то добавляет, если находит, то
#	возвращает True.

def wordSearch(c, x, test):

	b = c in test

	if b != True:
		test.add(c)
		return x + c
	else:
		return True