from person import Person

class Manager(Person):
	def giveRaise(this, percent, bonus=.10):
		Person.giveRaise(this, percent + bonus)