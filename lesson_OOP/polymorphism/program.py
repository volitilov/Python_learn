#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "polimorphism" ..........

#	Простой пример полМОРФИЙзма:
#	Есть клас в котором есть два метода один присваивает 
#	значение(количество закачек) переменной объекту user, 
#	а втрой использует значение переменной для подщёта 
#	сумарных закачек c нескольких пользователей. 

class UsersDownloads:
	def __init__(self, user, exdown, count):
		self.u = user
		self.e = exdown		# в роль для полиморфизма
		self.c = count
		self.record_us_d()
		self.allDownloads()

	def record_us_d(self):
		self.u['downloads'] = self.u['downloads'] + self.e


	def allDownloads(self):
		self.c['downloads'] = self.c['downloads'] + self.e