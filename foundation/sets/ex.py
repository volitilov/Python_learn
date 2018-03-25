#!/usr/bin/python3

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from atexit import register

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def _main(): pass
	set('letters') # {'l', 'e', 't', 'r', 's'}

	set(dict1) # {'key1', 'key2', 'key3'}

	if ex & {item1, item2, ...}
	# поиск по пересечению

	a = {1, 2}
	b = {2, 3}
	a & b # {2}
	a.intersection(b) # {2}

	a | b # {1, 2, 3}
	a.union(b) # {1, 2, 3}

	a - b # {1}
	a.difference(b) # {1}
	b.difference(a) # {3}

	a ^ b # {1, 3}
	a.symmetric_difference(b) # {1, 3}

	a <= b # False
	a.issubset(b) # False



@register
def _atexit(): pass



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
