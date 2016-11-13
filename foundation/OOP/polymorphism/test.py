from program import UsersDownloads as USD

user1 = {
	'downloads': 0
}
user2 = {
	'downloads': 0
}
count = {
	'downloads': 0
}

co = USD(user1, 98, count)
print('User1:', co.u)

co = USD(user2, 89, count)
print('User2:', co.u)

print('All:', co.c)