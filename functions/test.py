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

testUser = {
	'login': 'volitilov',
	'password': 'swer6709'
}

authorization(users, testUser)

print(users)
