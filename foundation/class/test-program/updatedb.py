#	updatedb ::::::::::::::::::::::::::::::::::::::::::::::

import shelve

db = shelve.open('persondb')

for key in sorted(db):
	print(key, '\t=>', db[key])

bob = db['Bob Dont']
bob.giveRaise(.10)
db['Bob Dont'] = bob
db.close()