import sys, os

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

inventary = {
	'верёвка': 1, 'фонарей': 6, 
	'золото': 42, 'нож': 1, 'стрелы': 12
}

def displayInventary(inventary):
	while True:
		inv = input('enter inventary: ')
		for i in inventary:
			if i == inv:
				os.system("echo '\e[92m{}: {}\e[0m'".format(i, inventary[i]))
				sys.exit(2)
			else: 
				os.system("echo '\e[31m{}\e[0m' '- not found'".format(inv))
				break


displayInventary(inventary)