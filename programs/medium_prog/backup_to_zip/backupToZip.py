#!/usr/bin/python3

# backupToZip.py
# Копирует папку вместе со всем её содержимым в ZIP-файл с 
# инкреминтируемым номером копии в имени файла.

# Использование: ./backupToZip.py

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, zipfile

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def backupToZip(folder):
	'''Создание резервной копии всего содержимого папки
	folder в виде ZIP-файла'''

	# убедиться в том, что задан обсалютный путь к файлу
	folder = os.path.abspath(folder)

	# Определить, какое имя файла должен использовать этот
	# код, исходя из имён уже существующих файлов
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

		if not os.path.exists(zipFilename): break
		number += 1

	# Создание ZIP-файла
	print('\nСоздаётся файл {}...\n'.format(zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# Обход всего дерева папки и сжатие файлов, содержащихся
	# в каждой папке.
	for folderName, subFolders, fileNames in os.walk(folder):
		os.system("echo 'Добавление файлов из папки:' \
			'\e[92m{}\e[0m'".format(folderName))

		# Добавить в ZIP-файл текущею папку
		backupZip.write(folderName)

		# Добавить в ZIP-файл все файлы из данной папки.
		for fileName in fileNames:
			newBase = os.path.basename(folder) + '_'
			if fileName.startswith(newBase) and fileName.endswith('.zip'):
				# не создовать резервный копии ZIP-файлов
				continue
			backupZip.write(os.path.join(folderName, fileName))
	
	backupZip.close()
	print('\nГотово.\n')


backupToZip('copy_files') 