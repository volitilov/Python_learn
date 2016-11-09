#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "inheritation" ..........

#	Task:

class SuperClass:
	def __init__(self, n, a):
		self.name = n
		self.age = a

	def outing(self):
		print(self.name, self.age)

class Security(SuperClass):
	def test(self):
		if self.name == 'oli':
			if self.age > '18':
				return True
			else:
				return False
		else:
			return False
