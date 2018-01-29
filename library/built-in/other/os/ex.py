import os, time

# ::::::::::::::::::::::::::::::::::::::::::::::::

for folderName, subfolders, filenames in os.walk('experement'):
	print('Текущая папка - ' + folderName)
	time.sleep(1)

	for subfolder in subfolders:
		print('Подпапка ' + folderName + ': ' + subfolder)
		time.sleep(1)

	for filename in filenames:
		print('Файл в папке ' + folderName + ': ' + filename)
		time.sleep(1)

	print('')
# Текущая папка - experement
# Подпапка experement: ex2
# Подпапка experement: ex1
# Файл в папке experement: ex_file.py

# Текущая папка - experement/ex2
# Файл в папке experement/ex2: ex_file4.py

# Текущая папка - experement/ex1
# Подпапка experement/ex1: ex_1
# Файл в папке experement/ex1: ex_file2.py

# Текущая папка - experement/ex1/ex_1
# Файл в папке experement/ex1/ex_1: ex_file3.py






for folderName, subfolders, files in os.walk('experement'):
	print('foldername: ', folderName)
	print('derictories: ', subfolders)
	print('files: ', files)
# foldername:  experement
# derictories:  ['ex2', 'ex1']
# files:  ['ex_file.py']
# foldername:  experement/ex2
# derictories:  []
# files:  ['ex_file4.py']
# foldername:  experement/ex1
# derictories:  ['ex_1']
# files:  ['ex_file2.py']
# foldername:  experement/ex1/ex_1
# derictories:  []
# files:  ['ex_file3.py']

