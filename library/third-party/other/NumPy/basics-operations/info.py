#	///////////////////////////////////////////////////////////////////
#	Базовые операции ..................................................

#	Математические операции над массивами выполняются поэлементно. 
#	Создается новый массив, который заполняется результатами действия 
#	оператора.

	import numpy as np

	a = np.array([20, 30, 40, 50])
	b = np.arange(4)
	a + b 	# array([20, 31, 42, 53])
	a - b 	# array([20, 29, 38, 47])
	a * b 	# array([  0,  30,  80, 150])
	
	a / b  # При делении на 0 возвращается inf (бесконечность)
	# array([         inf,  30.        ,  20.        ,  16.66666667])
	# <string>:1: RuntimeWarning: divide by zero encountered in true_divide
	
	a ** b 	# array([     1,     30,   1600, 125000])

	a % b  # При взятии остатка от деления на 0 возвращается 0
	# <string>:1: RuntimeWarning: divide by zero encountered in remainder
	# array([0, 0, 0, 2])

#	Для этого, естественно, массивы должны быть одинаковых размеров.

	c = np.array([[1, 2, 3], [4, 5, 6]])
	d = np.array([[1, 2], [3, 4], [5, 6]])
	c + d

	# Traceback (most recent call last):
	#   File "<input>", line 1, in <module>
	# ValueError: operands could not be broadcast together with shapes (2,3) (3,2)

#	Также можно производить математические операции между массивом и числом. 
#	В этом случае к каждому элементу прибавляется (или что вы там делаете) 
#	это число.

	a + 1 	# array([21, 31, 41, 51])
	a ** 3 	# array([  8000,  27000,  64000, 125000])
	
	a < 35  # И фильтрацию можно проводить
	# array([ True,  True, False, False], dtype=bool)

#	NumPy также предоставляет множество математических операций для обработки 
#	массивов:

	np.cos(a)
	# array([ 0.40808206,  0.15425145, -0.66693806,  0.96496603])
	
	np.arctan(a)
	# array([ 1.52083793,  1.53747533,  1.54580153,  1.55079899])
	
	np.sinh(a)
	# array([  2.42582598e+08,   5.34323729e+12,   1.17692633e+17,
	#          2.59235276e+21])

#	Многие унарные операции, такие как, например, вычисление суммы всех 
#	элементов массива, представлены также и в виде методов класса ndarray.

	a = np.array([[1, 2, 3], [4, 5, 6]])
	np.sum(a) 	# 21
	a.sum() 	# 21	
	a.min() 	# 1
	a.max() 	# 6

#	По умолчанию, эти операции применяются к массиву, как если бы он был 
#	списком чисел, независимо от его формы. Однако, указав параметр axis, 
#	можно применить операцию для указанной оси массива:

	a.min(axis=0)  # Наименьшее число в каждом столбце
	# array([1, 2, 3])
	
	a.min(axis=1)  # Наименьшее число в каждой строке
	# array([1, 4])