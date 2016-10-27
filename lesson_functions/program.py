#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "function" ////////////////

#	Task:

#	Сделать программу авторизации, проверять наличие логина и 
#	пароля в словаре, если нет, то сохранить в словарь.


def authorization(users, testUser):

	for i in users:
		if i['login'] == testUser['login']:
			if i['password'] != testUser['password']:
				user3 = testUser
				users.append(user3)
