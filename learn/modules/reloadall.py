'''
reloadall.py: транзитивная перезагрузка вложенных модулей
'''

import types
from imp import reload 	# требуется в версии 3.0

def status(module):
	print('reloading ' + module.__name__)

def transitive_reload(module, visited):
	if not module in visited:	# Пропустить повторные посещения
		status(module)			# Перезагрузить модуль
		reload(module)			# И посетить дочерние модули
		visited[module] = None
		
		for attrobj in module.__dict__.values(): # Для всех атрибутов
			if type(attrobj) == types.ModuleType: # Рекурсия, если модуль
				transitive_reload(attrobj, visited)

def reload_all(*args):
	visited = {}
	for arg in args:
		if type(arg) == types.ModuleType:
			transitive_reload(arg, visited)

if __name__ == '__main__':
	import reloadall
	reload_all(reloadall)	# Тест: перезагрузить самого себя
							# Должна перезагрузить этот модуль и модуль types