#	Manager :::::::::::::::::::::::::::::::::::::::::::::

from person import Person

class Manager(Person):
	'''
	Версия класса Person, адаптированная в соответствии
	со специальными требованиями
	'''
	def __init__(this, name, pay):
		Person.__init__(this, name, 'manager', pay)
	def giveRaise(this, percent, bonus=.10):
		Person.giveRaise(this, percent + bonus)

#	or ::::::::::::::::::::::::::::::::::::::::::::::::::

'''
class Manager:
	def __init__(this, name, pay):
		this.person = Person(name, 'manager', pay)
	def giveRaise(this, percent, bonus=.10):
		this.person.giveRaise(percent + bonus)
	def __getattr__(this, attr):
		return getattr(this.person, attr)
	def __str__(this):
		return str(this.person)
'''