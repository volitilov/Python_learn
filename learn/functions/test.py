#	ex1 .............................................

def test1(var1):
	count = var1
	def test2(var2):
		nonlocal count
		print(var2, count)
		count += 1
	return test2

f = test1(1)
f('name1 - ') 	# name1 - 1
f('name2 - ')	# name2 - 2 

g = test1(10)
g('nameG1 - ') 	# nameG1 - 10
g('nameG2 - ') 	# nameG2 - 11

f('name3 - ')	# name3 - 3
g('nameG3 - ') 	# nameG3 - 12

#	ex2 ...............................................

def func(arg1, arg2, arg3=0, arg4=0):
	print(arg1, arg2, arg3, arg4)

func(1, 2)						# 1, 2, 0, 0
func(1, arg4=1, arg2=0)			# 1, 0, 0, 1
func(arg1=1, arg2=0)			# 1, 0, 0, 0
func(arg3=1, arg2=2, arg1=3)	# 3, 2, 1, 0
func(1, 2, 3, 4)				# 1, 2, 3, 4

#	ex3 ................................................

import sys
from tkinter import Button, mainloop

x = Button(text ='Press me', command=(lambda:sys.stdout.write('Spam\n')))
x.pack()
mainloop()

#	ex4 ................................................

def timesfour(S):
	for i in S:
		yield i * 4

G = timesfour('spam')
print(list(G))		# ['ssss', 'pppp', 'aaaa', 'mmmm']