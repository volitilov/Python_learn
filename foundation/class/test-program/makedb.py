#	import modules ::::::::::::::::::::::::::::::::::::::::::::

from person import Person
from manager import Manager

bob = Person('Bob Dont')
alex = Person('Alex Rudin', 'developer')
tom = Manager('Tom Piterson', 5000)

import shelve

db = shelve.open('persondb')
for object in (bob, alex, tom):
	db[object.name] = object
db.close()