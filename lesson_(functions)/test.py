from program import *

user1 = {
	'login': 'volitilov',
	'password': '6709'
}

user2 = {
	'login': 'olitilo',
	'password': 'S6709'
}

users = [user1, user2]

newUser = {
	'login': 'test',
	'password': '999'
}

print(authorization(users, newUser))