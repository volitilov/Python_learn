#!/usr/bin/python3
# mcb.pyw - Сохраняет и загружает фрагменты текста
# 			в буфер обмена.

# Использование:
# 	- python3 mcb.pyw save <ключевое слово> - 
# 		сохраняет из буфера обмена значение ключевое слово
# 	- python3 mcb.pyw <ключевое слово> -
# 		загружает значение ключевого слова в буфер обмена
# 	- python3 mcb.pyw list -
# 		загружает все ключевые слова в буфер обмена
#	- python3 mcb.pyw delete <ключевое слово> - 
# 		удалить значение по ключу из хранилища
#	- python3 mcb.pyw deleteall -
#		очистить хранилище

# Пример: 	./mcb.pyw save 'example'
#			./mcb.pyw 'example'
# 			./mcb.pyw list
# 			./mcb.pyw delete 'example'
# 			./mcb.pyw deleteall

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import shelve, pyperclip, sys

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

mcbShelf = shelve.open('mcb_data')

# сохранение содержимого в базу из буфера обмена
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
	# загрузка списком содержимого из базы в буфер обмена
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	# очистка базы
	elif sys.argv[1].lower() == 'deleteall':
		mcbShelf.clear()
	# загрузка значения из хранилища в буфер, по ключу 
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

# удаление содержимого из бызы по ключу
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	del mcbShelf[sys.argv[2]]

mcbShelf.close()