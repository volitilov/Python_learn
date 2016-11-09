#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "if, elif, else" ////////

#	Программа которая проверяет условия перед запуском другой 
#	программы.

def purchases():
	return True

def balanceAudit(user):

	if user['balance'] != '0':
		return purchases()
	else:
		return False