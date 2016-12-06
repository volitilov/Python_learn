'''
Программа, которая подсчитывает количество строк и символов 
в файле.
'''

def countLines(name):
	'''
	Функция countLines(name), читает входной файл и подсчитывает
	число строк в нем.
	'''
	L = len([line for line in open(name)])
	print('Число строк: {}'.format(L))



def countChars(name):
	'''
	Функция countChars(name), читает входной файл и подсчитывает 
	число символов в нем без пробелов.
	'''
	C = []
	for x in open(name):
		for y in x:
			if y == ' ':
				continue
			else:
				C.append(y)
	print('Число символов: ' + str(len(C)))

def test(name):
	'''
	Функция test(name), вызывает две предыдущие функции с 
	заданным именем файла.
	'''
	countLines(name)
	countChars(name)

if __name__ == '__main__':
	import mymod
	test('test.py')