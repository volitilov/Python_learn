import os, sys

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

inventary = {
	'верёвка': 1, 'фонарь': 6, 
	'золото': 42, 'нож': 1, 'стрелы': 12
}

dragonLoot = ['золото', 'нож', 'золото', 'рубин']


def add_to_inventary(inventary, addedItems):
	"""Добавляет нивентарь в число имеющегося"""
	for i in dragonLoot:
		if (i in inventary): 
			inventary[i] += 1
		else: inventary[i] = 1

	return inventary



a = add_to_inventary(inventary, dragonLoot)
print(a)


