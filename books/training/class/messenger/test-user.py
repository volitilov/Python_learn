#	create 	users ::::::::::::::::::::::::::::::::::::::::::
from user import User

bob = User('Bob', '123')
i01 = User('i01', 'faint')
sam = User('Sam', 'qwe')
# ban = User('Ban', '8787')

#	test registration ::::::::::::::::::::::::::::::::::::::

# bob.registration()
# i01.registration()
# sam.registration()
# ban.registration()

#	test login :::::::::::::::::::::::::::::::::::::::::::::

# bob.login()
# i01.login()
# sam.login()
# ban.login()

#	test addFriends ::::::::::::::::::::::::::::::::::::::::

# bob.addFriend('Bob')
# i01.addFriend('Bob')
# sam.addFriend('Bob')
# ban.addFriend('Bob')

#	test users-db ::::::::::::::::::::::::::::::::::::::::::

import shelve

d = shelve.open('users-db')

print(list(d))

for key in d:
	print(d[key])

# print(d['Bob'].__class__) 	# <class 'user.User'>
# print(d['Bob'].__class__.__name__) 	# User
# print(list(d.__dict__.keys())) 	# ['writeback', 'dict', '_protocol', 'cache', 'keyencoding']


# print('\n',
# 	'База usersdb:\n',
# 		'\n',
# 		'- type: {}'.format(type(d)), '\n',
# 		'- keys {}:'.format(len(list(d))), sorted(list(d)), '\n',
# 		'- values {}:'.format(list(d.values())), '\n',
# 		'- items {}:'.format(list(d.items())), '\n',
# 		'- {} moduls:'.format(len([d])), d,
# 	'\n')

# for key in sorted(d):
# 	print(' -', key + ':\t', type(d[key]))

# print(d['Bob'].username, d['Bob'].password, d['Bob'].friends)

# del d['2']
# d.clear()

# d['1'] = d['2']

d.close()