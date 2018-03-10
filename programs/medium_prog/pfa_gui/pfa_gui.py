#!/usr/bin/python3

# Приnожение с графическим поnьзоватеnьским интерфейсом, в котором
# применяется механизм PFA дnя создания дорожных знаков 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showerror, showwarning

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	WARN = 'warn'
	CRIT = 'crit'
	REGU = 'regu'

	SIGNS = {
		'do not enter': CRIT,
		'railroad crossing': WARN,
		'55\nspeed limit': REGU,
		'wrong way': CRIT,
		'merging traffic': WARN,
		'one way': REGU
	}

	crit_CB = lambda: showerror('Error', 'Error Button Pressed!')
	warn_CB = lambda: showwarning('Warning', 'Warning Button Pressed!')
	info_CB = lambda: showinfo('Info', 'Info Button Pressed!')

	top = Tk()
	top.geometry('250x300')
	top.title('Road Signs')

	# формируются шаблон класса Button и кор­невое окно top. Эrо 
	# означает, что при каждом вызове в проrрамме объекта MyButton
	# этот объект вызывает Button (метод Tkinter.Button() создает 
	# кнопку) с указанием top в качестве первоrо параметра.
	My_button = pto(Button, top)
	
	# применяется первый созданный объект, MyButton, и на ero 
	# основе создаются шаблоны
	Crit_button = pto(My_button, command=crit_CB, bg='white', fg='red')
	Warn_button = pto(My_button, command=warn_CB, bg='yellow')
	Regu_button = pto(My_button, command=info_CB, bg='white')

	for each_sign in SIGNS:
		sign_type = SIGNS[each_sign]
		# Формируется строка, которую может вы­числить интерпретатор 
		# Python, включающая имя создаваемой кнопки, в качестве 
		# текстового параметра передается метка на кнопке, затем к 
		# пара­метрам применяется метод pack(). Если формируемый знак 
		# является за­прещающим, то буквы метки на кнопке преобразуются 
		# в прописные, в про­тивном случае в прописную преобразуются 
		# первые буквы каждого слова в метке.
		cmd = '%s_button(text=%r%s).pack(fill=X)' % (
			sign_type.title(), each_sign,
			'.upper()' if sign_type == CRIT else '.title()')
		# порождение экземпляра каждой кнопки
		eval(cmd)

	Button(top, 
		text='quit',
		command=top.quit,
		bg='red',
		fg='white').pack(expand=True)

	top.mainloop()