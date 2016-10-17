# ////////////////////////////////////////////////////////////
# Множества (set и frozenset). ///////////////////////////////

# Множество в python - "контейнер", содержащий не повторяющиеся 
# 	элементы в случайном порядке.

a = set() 					# создаём множество
a = {'a', 'b', 'c', 'd'} 	# так тоже можно

# методы работы с множествами
len(s) 			# число элементов в множестве (размер множества).
x in s 			# принадлежит ли x множеству s.
set == other	# все элементы set принадлежат other, все элементы other принадлежат set.
set.copy() 		# копия множества.

set.isdisjoint(other) 	# истина, если set и other не имеют общих элементов.

set.issubset(other) или set <= other					# все элементы set принадлежат other.
set.union(other, ...) или set | other | ... 			# объединение нескольких множеств.
set.intersection(other, ...) или set & other & ... 		# пересечение.
set.difference(other, ...) или set - other - ... 		# множество из всех элементов set, не принадлежащие ни одному из other.
set.symmetric_difference(other); set ^ other 			# множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.

# и операции, непосредственно изменяющие множество:
set.update(other, ...); set |= other | ... 					# объединение.
set.intersection_update(other, ...); set &= other & ... 	# пересечение.
set.difference_update(other, ...); set -= other | ... 		# вычитание.
set.symmetric_difference_update(other); set ^= other 		# множество из элементов, встречающихся в одном множестве, 
															# 	но не встречающиеся в обоих.
set.add(elem) 		# добавляет элемент в множество.
set.remove(elem) 	# удаляет элемент из множества. KeyError, если такого элемента не существует.
set.discard(elem) 	# удаляет элемент, если он находится в множестве.
set.pop() 			# удаляет первый элемент из множества. Так как множества не упорядочены, 
					# 	нельзя точно сказать, какой элемент будет первым.
set.clear()			# очистка множества.