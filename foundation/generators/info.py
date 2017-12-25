# Generators :::::::::::::::::::::::::::::::::::::::::::::::::::



# генератор чисел ..............................................

range(0, 10, 2)




# генератор списков ............................................

# близкий родственник цикла for, который позволяет применять 
# выражение к элементам итерируемой последовательности.

L = [1, 2, 3, 4, 5]
[x + 5 for x in L]	# [6, 7, 8, 9, 10]

list(open('test.py'))

[line.rstrip() for line in open('test.py')]
[line.rstrip() for line in open('test.py') if line[0] == 'p']

[x + y for x in 'abc' for y in 'def']
list(x + y for x in 'abc' for y in 'def')

[i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[(row, cols) for row in rows for col in cols]





# генератор множеств ...........................................

set(open('test.py'))

{line for line in open('test.py')}
{line for line in open('test.py') if line[0] == 'p'}

{x * x for x in range(10)}
set(x * x for x in range(10))




# генератор словарей ...........................................

dict(open('test.py'))

{ix: line for ix in enumerate(open('test.py'))}
{ix: line for ix in enumerate(open('test.py')) if line[0] == 'p'}

{x: x * x for x in range(10)}
dict((x, x * x) for x in range(10))