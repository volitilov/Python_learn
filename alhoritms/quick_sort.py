def quick_sort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		return quick_sort(less) + [pivot] + quick_sort(greater)


ex = [5, 1, 3, 7, 9, 2, 17]
ex_list = list(range(1, 99999))

ex_list.reverse()

# print(quick_sort(ex_list))
print(sorted(ex_list))