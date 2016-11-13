from program import *

user = {
	'balance': '566'
}

testUser = {
	'balance': '0'
}
user['balance'] = '0'

print('Balance: ', balanceAudit(user))