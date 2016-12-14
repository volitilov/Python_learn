import shelve
data_b = 'users-db'

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.friends = []
		self.log_in = False

	def registration(self): 
		db = shelve.open(data_b)

		for key in sorted(db):
			if (db[key].username, db[key].password) == (self.username, self.password):
				raise Exception('Пользователь {} есть в базе.'.format(self.username))
		
		db['{}'.format(len(list(db)) + 1)] = self

		db.close()

	def login(self):
		db = shelve.open(data_b,  writeback=True)
		
		for key in sorted(db):
			# reg = False if (db[key].username, db[key].password) != (self.username, self.password) else True
			if (db[key].username, db[key].password) == (self.username, self.password):
				db[key].log_in = True
				break
			else:
				db[key].log_in = False

		if db[key].log_in == False:
			raise Exception('{} регестрируйся.'.format(self.username))

		db.close()

	def addFriend(self, name):
		ad_fr = False
		ad_fr2 = False

		db = shelve.open(data_b,  writeback=True)

		for i in sorted(db):
			if name == db[i].username:
				ad_fr = True
				break
			else:
				ad_fr = False
		
		for key in sorted(db):
			if (db[key].username, db[key].password) == (self.username, self.password):
				if db[key].log_in == True:
					fr = name in db[key].friends
					if fr == True: 
						raise Exception('Вы с {} уже друзья.'.format(name))
					else:
						if ad_fr == True:
							db[key].friends.append(name)
							ad_fr2 = True
							break
				else:	
					raise Exception('{} авторизуйся.'.format(self.username))

		if ad_fr == False:
			raise Exception('Пользователь {}, не зарегестрирован.'.format(name))

		if ad_fr2 == False:
			raise Exception('{}: не зарегестрирован.'.format(name))

		db.close()

	def gatherAttrs(self):
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('{}: {}'.format(key, getattr(self, key)))
		return ', '.join(attrs)

	def __str__(self):
		return '[{} => {}]'.format(self.__class__.__name__, self.gatherAttrs())
