#!/usr/bin/python3

# Проrрамма с rрафическим пользовательским интерфейсом, 
# предназначенная для навиrации по файловой системе

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os
from time import sleep
from tkinter import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Dir_List(object):
	def __init__(self, initdir=None):
		self.top = Tk()
		# создаёт заголовок главного приложения
		self.label = Label(self.top, text='Directory Lister v1.1')
		self.label.pack()

		# задаётся имя текущего котолога
		self.cwd = StringVar(self.top)

		# служит для отображении имени текущего котолога
		self.dirl = Label(self.top, fg='blue',
			font=('Helvetica', 12, 'bold'))
		self.dirl.pack()

		# В этом разделе определяется основная часть применяемого 
		# rрафического пользо­вательского интерфейса, объект Listbox 
		# с именем dirs, который содержит листинг файлов 
		# рассматриваемого каталога. Применяется объект Scrollbar, 
		# позволяющий пользователю прокручивать листинг, если 
		# количество файлов превышает размер объекта Listbox по 
		# вертикали. Оба этих графических элемента содержатся в 
		# rрафи­ческом элементе Frame. Элементы Listbox имеют 
		# обратный вызов (setDirAndGo), привязанный к ним с 
		# использованием метода Ьind() Listbox.
		# Под привязкой подразумевается установление соответствия 
		# между нажатием кла­виши, действием мышью или каким-то 
		# другим событием и обратным вызовом, кото­рый выполняется 
		# при формировании такого события пользователем. Вызов 
		# функции setDirAndGo() происходит после двойного щелчка на 
		# одном из элементов в списке Listbox. Привязка элемента 
		# Scrollbar к элементу Listbox осуществляется путем вызова 
		# метода Scrollbar.config().
		self.dirfm = Frame(self.top)
		self.dirsb = Scrollbar(self.dirfm)
		self.dirsb.pack(side=RIGHT, fill=Y)
		self.dirs = Listbox(self.dirfm, height=15,
			width=50, yscrollcommand=self.dirsb.set)
		self.dirs.bind('<Double-1>', self.setDirAndGo)
		self.dirsb.config(command=self.dirs.yview)
		self.dirs.pack(side=LEFT, fill=BOTH)
		self.dirfm.pack()

		# создается поле ввода Entry, в котором пользователь может 
		# ввести имя ка­талога, в который требуется перейти и 
		# просмотреть содержащиеся в нем файлы с помощью элемента 
		# Listbox. К этому полю ввода добавлена привязка к клавише
		# <Enter>, чтобы пользователь мог нажимать эту клавишу 
		# возврата вместо щелчка кнопкой. Эго относится и к привязке 
		# мыши, которая рассматривалась ранее, приме­нительно к 
		# элементу Listbox. После того как пользователь дважды щелкнет 
		# на эле­менте в списке Listbox, осуществляется такое же 
		# действие, как при вводе имени ка­талога вручную в поле ввода 
		# Entry с последующим щелчком на кнопке Go (Перейти).
		self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
		self.dirn.bind('<Return>', self.doLS)
		self.dirn.pack()

		# определяется рамка Button (Ьfm) для размещения в ней трех 
		# кнопок: кноп­ки "очистки" (clr), кнопки "перехода" (ls) и 
		# кнопки "завершения" (quit). С каждой кнопкой связаны 
		# собственная конфиrурация и обратный вызов, активизируемый 
		# по­сле щелчка на ней.
		self.bfm = Frame(self.top)
		self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
			activeforeground='white', activebackground='blue')
		self.ls = Button(self.bfm, text='List Directory', 
			command=self.doLS, activebackground='green', 
			activeforeground='white')
		self.quit = Button(self.bfm, text='Quit', command=self.top.quit,
			activeforeground='white', activebackground='red')
		self.clr.pack(side=LEFT)
		self.ls.pack(side=LEFT)
		self.quit.pack(side=LEFT)
		self.bfm.pack()

		# инициализируется программа GUI, действие которой 
		# начинается с текущего рабочего ка­талога.
		if initdir:
			self.cwd.set(os.curdir)
			self.doLS


	# очищает строковую переменную Tk с именем cwd, которая со­держит 
	# имя текущего активного каталога. Эга переменная используется для 
	# отсле­живания того, какой каталог рассматривается в данный момент, 
	# и, что более важно, помогает отслеживать предыдущий каталог на 
	# случай, если возникнут ошибки
	def clrDir(self, ev=None):
		self.cwd.set('')


	# задает каталог, в котором необходимо получить листинг файлов, 
	# и формирует вызов метода, с помощью которого осуществляется это 
	# дей­ствие, doLS().
	def setDirAndGo(self, ev=None):
		self.last = self.cwd.get()
		self.dirs.config(selectbackground='red')
		check = self.dirs.get(self.dirs.curselection())

		if not check: check = os.curdir

		self.cwd.set(check)
		self.doLS


	# В данном выполняются все предохранительные проверки (например, 
	# содержит ли тек­стовая строка имя каталога и существует ли этот 
	# каталог). Если возникает какая-либо ошибка, то в качестве 
	# текущего каталога снова устанавливается последний каталог. Если 
	# же ошибка не обнаруживается, то происходит вызов метода os.listdir() 
	# для получения фактических данных о файлах, присутствующих в каталоге, 
	# и с помощью этих данных происходит замена листинга в элементе 
	# Listbox. В то время как в фоно­вом режиме продолжается работа по 
	# выборке информации из нового каталога, си­няя полоса, выделенная 
	# подсветкой, становится ярко красной. После окончательного перехода в 
	# новый каталог восстанавливается синий цвет полосы.
	def doLS(self, ev=None):
		error = ''
		tdir = self.cwd.get()

		if not tdir: tdir = os.curdir

		if not os.path.exists(tdir):
			error = tdir + ': no such file'
		elif not os.path.isdir(tdir):
			error = tdir + ': not a directory'

			if error: self.cwd.set(error)

			self.top.update()
			sleep(2)

			if not (hasattr(self, 'last') and self.last):
				self.last = os.curdir

			self.cwd.set(self.last)
			self.dirs.config(selectbackground='LightSkyBlue')
			self.top.update()

			return

		self.cwd.set('FEТCHING DIRECТORY CCNТENТS...')
		self.top.update()
		dirlist = os.listdir(tdir)
		dirlist.sort()
		os.chdir(tdir)
		self.dirl.config(text=os.getcwd())
		self.dirs.delete(0, END)
		self.dirs.insert(END, os.curdir)
		self.dirs.insert(END, os.pardir)
		for eachFile in dirlist:
			self.dirs.insert(END, eachFile)
		self.cwd.set(os.curdir)
		self.dirs.config(selectbackground='LightSkyBlue')


def _main():
	d = Dir_List(os.curdir)
	mainloop()

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
