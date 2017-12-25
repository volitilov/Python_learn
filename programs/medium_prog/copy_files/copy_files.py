#!/usr/bin/python3

# copy_files.py 
# выполняет обход дерева коталогов с целью отбора и 
# копирования файлов с заданным расширением

# Использование: ./copy_files.py [commands] [args]
# [commands]:
# 	copy [ext] - обойти дерево коталогов и скопировать файлы
# 				с заданным расширением в виде списка во временное 
# 				хранилище, начиная с текущей дериктории
# 	paste folder_name - всавить в заданную дерикторию

# Пример: 	./copy_files.py copy '.pdf'
#			./copy_files.py paste 'folder_name'

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, sys, shelve, shutil, logging

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

logging.basicConfig(
	filename='my_program_log.txt',
	level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s - %(message)s')


def copy_files_in_tree(ext):
	# получение обсолютного пути текущей дериктории
	folder = os.path.abspath('')
	files = []

	# обход дерева котологов с целью найти файлы с заданным
	# расширением, найденные файлы внести в список
	for folderName, _, fileNames in os.walk(folder):
		for file in fileNames:
			if file.endswith(ext):
				files.append(folderName + '/' + file)

	# копирование списка файлов во временное хранилище
	db = shelve.open('files_list')
	db['files'] = files
	print(files)
	db.close()


# вставка в заданную дерикторию
def paste_files(folder_name):
	logging.debug(folder_name)
	# получение списока файлов из хранилища
	db = shelve.open('files_list')
	files = db['files']

	# если дериктория не создана создаём
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)
	# копирование и вставка файлов в заданную дерикторию
	for file in files:
		# fileName = file.split('/')
		# получение название фала
		fileName = os.path.basename(file)
		# копирование файла
		shutil.copy(os.path.relpath(file), folder_name+'/'+fileName)

	db.close()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# получение названия расширения
if len(sys.argv) == 3 and sys.argv[1].lower() == 'copy':
	ext = str(sys.argv[2])
	copy_files_in_tree(ext)

# получение название дериктории в которую необходму 
# скопировать
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'paste':
	folder_name = str(sys.argv[2])
	paste_files(folder_name)

elif len(sys.argv) < 3:
	print('Использование: ./copy_files.py [commands] [args] \
			\n[commands]:\n \
			\ncopy [ext] - обойти дерево коталогов и скопировать файлы \
			\nс заданным расширением в виде списка во временное \
 			\nхранилище, начиная с текущей дериктории\n \
		 	\npaste [folder_name] - всавить в заданную дерикторию\n \
		 	\nПример: \
		 	\n./copy_files.py copy ".pdf" \
			\n./copy_files.py paste "folder_name"')

