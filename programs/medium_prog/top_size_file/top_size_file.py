#!/usr/bin/python3

# Назначение: top_size_file.py
# поиск самых больших файлов в дереве коталогов

# Использование: ./top_size_file.py [count]
# [count] - кол-во искомых файлов, начиная
# 			с самого большого

# Пример: ./top_size_file.py 10

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

import sys, os, heapq, random

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# поиск заданного кол-ва файлов в дереве котологов с 
# максимальным размером
def top_size_files(count):
	# убедиться в том, что задан обсалютный путь к 
	# текущей дериктории
	folder = os.path.abspath('')
	all_files = []

	# обход дерева котологов
	for folderName, _, files in os.walk(folder):
		for file in files:
			# получение размера файла
			size = os.path.getsize(folderName+'/'+file) / 1000
			obj = {
				'name': file,
				'size': round(size)
			}
			all_files.append(obj)

	# получение заданного количества файлов, 
	# отсортированного по размеру 
	results = heapq.nlargest(count, all_files, key=lambda s: s['size'])
	
	return results



if len(sys.argv) == 2 and sys.argv[1].isdigit():
	files = top_size_files(int(sys.argv[1]))
	for i in files:
		os.system("echo '\e[92m{:.<10}кб.\e[0m' \
			'{}'".format(i['size'], i['name']))

elif len(sys.argv) < 2:
	print('\nНазначение: top_size_file.py')
	print('- поиск самых больших файлов в дереве коталогов')
	print('\nИспользование: ./top_size_file.py [count]')
	print('[count] - кол-во искомых файлов, начиная с самого большого\n')
	print('Пример: ./top_size_file.py 10\n')

