import shelve

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.friends = []
		self.addFr = False
		self.sendMess = False

	def registration(self): 
		db = shelve.open('users-db')

		for key in sorted(db):
			if (db[key].username, db[key].password) == (self.username, self.password):
				raise Exception('Пользователь {} есть в базе.'.format(self.username))
		
		db['{}'.format(len(list(db)) + 1)] = self

		db.close()

	def login(self):
		reg = False

		db = shelve.open('users-db',  writeback=True)
		
		for key in sorted(db):
			# reg = False if (db[key].username, db[key].password) != (self.username, self.password) else True
			if (db[key].username, db[key].password) != (self.username, self.password):
				reg = False
			else:
				reg = True
				break

		if reg == True:
			db[key].addFr = True
			db[key].sendMess = True	
		else:
			raise Exception('{} регестрируйся.'.format(self.username))

		db.close()
		# print(reg)

	def addFriend(self, name):
		ad_fr = False
		fr_name = False

		db = shelve.open('users-db',  writeback=True)

		for key in sorted(db):
			if db[key].username == name:	# неверно 
				raise Exception('Вы с {} уже друзья.'.format(name))
			elif db[key].addFr != True:
				raise Exception('{} авторизуйся.'.format(self.username))
			else:
				fr_name = False

			if (db[key].username, db[key].password) != (self.username, self.password):
				ad_fr = False
			else:
				if db[key].addFr == True:
					ad_fr = True
					break

		if ad_fr == False:
			raise Exception('{} регестрируйся.'.format(self.username))

		if fr_name == False and ad_fr == True:
			db[key].friends.append(name)

		db.close()

	def gatherAttrs(self):
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('{}: {}'.format(key, getattr(self, key)))
		return ', '.join(attrs)

	def __str__(self):
		return '[{} => {}]'.format(self.__class__.__name__, self.gatherAttrs())


# user = new User('lalka', 'azaza')

# user.registration()

# user.login()

# user.addFriend('vasya')

# user.sendMessage('vasya', 'hello')

# user.log('vasya')

# [ { from: 'lalka', to: 'vasya', text: 'hello' } ]


# def sendMessage(self, to, text):
# 	msg = new Message(self.username, to, text)
