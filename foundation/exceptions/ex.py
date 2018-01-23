while True:
	try:
		tuna = int(input('Сколько тебе лет?\n'))
		break
	except ValueError:
		print('Ведите цифру')
	except ZeroDivisionError:
		print('Тебе не может быть {}'.format(tuna))
	finally:
		print('Этот блок выпоняеться независимо от ошибок')


print(tuna)