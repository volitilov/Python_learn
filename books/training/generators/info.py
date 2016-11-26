#	Generators :::::::::::::::::::::::::::::::::::::::::::::::::::

#	

#	генератор списков ............................................

#	близкий родственник цикла for, который позволяет применять 
#	выражение к элементам итерируемой последовательности.

L = [1, 2, 3, 4, 5]
L = [x + 5 for x in L]	# [6, 7, 8, 9, 10]

list(open('test.py'))

[	line.rstrip() for line in open('test.py')
				  for line in open('test.py') if line[0] == 'p'
]

[x + y for x in 'abc' for y in 'def']

#	генератор множеств ...........................................

set(open('test.py'))

{	line for line in open('test.py')
		 for line in open('test.py') if line[0] == 'p'
}

#	генератор словарей ...........................................

dict(open('test.py'))

{	ix: line for ix in enumerate(open('test.py'))
			 for ix in enumerate(open('test.py')) if line[0] == 'p'
}