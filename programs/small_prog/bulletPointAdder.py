#!/usr/bin/python3

# bulletPointAdder.py 
# Добавляет маркеры Википедии в начало каждой строки теста, 
# сохранённого в буфере обмена.


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import pyperclip

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

text = pyperclip.paste()

# разделяет строки и добавляет звёздочки
lines = text.split('\n')

# цикл по списку lines добавляет звёздочку в каждую строку
# в списке lines
for i in lines:
	lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)