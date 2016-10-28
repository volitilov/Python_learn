#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "loop" //////////////////

#	Task:

#	Программа генирации парного ключа, один идёт user, другой
#	admin. Есть регулировка сложности.


def createKey(random, letters, number, complexity, key):

	a = list(letters)
	b = list(number)
	c = random.randrange(1, len(a))
	d = random.randrange(1, len(b))

	i = 0
	while i <= complexity:
		key.append(a[c])
		key.append(b[d])
		i += 1 

	key = ''.join(key)
	return key

def recordKey(key, user, admin):
	user['key'] = ''.join(key)
	admin['key'] = ''.join(key)

	return admin
