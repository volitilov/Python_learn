#!/usr/bin/python3

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from tkinter import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	def resize(ev=None):
		label.config(font='Helvetica -{} bold'.format(scale.get()))

	top = Tk()
	top.geometry('300x150')

	label = Label(top, 
		text='Hello World!',
		font='Helvetica -12 bold')
	label.pack(fill=Y, expand=1)

	scale = Scale(top,
		from_=10,
		to=40,
		orient=HORIZONTAL,
		command=resize)
	scale.set(12)
	scale.pack(fill=X, expand=1)

	quit = Button(top, 
		text='quit', 
		command=top.quit,
		# bg='red',
		# fg='white')
		activeforeground='white',
		activebackground='red')
	quit.pack(expand=1)



	mainloop()
