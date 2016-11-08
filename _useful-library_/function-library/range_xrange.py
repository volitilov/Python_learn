#   //////////////////////////////////////////////////////////
#   range and xrange .........................................

	range() 
#	является универсальной функцией питона для создания списков
#	(list) содержащих арифметическую прогрессию. Чаще всего она 
#	используется в циклах for. Функция range() может принимать 
#	от одного до трех агрументов, при этом аргументами должны 
#	быть целые числа (int). range(старт, стоп, шаг) - так 
#	выглядит стандартный вызов функции range() в Python. По 
#	умолчанию старт равняется нулю, шаг единице.

#	Возвращает список целых чисел в форме 
#	[старт, старт + шаг, старт + шаг*2...]. 
#	Если шаг положительное число, последним элементом списка 
#	будет наибольшее старт + i * шаг меньшее числа стоп. Если 
#	шаг отрицательное число, то последний элемент будет 
#	наименьшее старт + i * шаг большее числа стоп. Шаг не должен 
#	равняться нулю, иначе возникнет ValueError.

	range(7) 			# [0, 1, 2, 3, 4, 5, 6]
	range(1,8)			# [1, 2, 3, 4, 5, 6, 7]
	range(0, 20, 5) 	# [0, 5, 10, 15]
	range(0, -7, -1)	# [0,-1,-2,-3,-4,-5,-6]
	range(1, 0)			# []
 
#	Функция xrange() в Python очень похожа на функцию range() за 
#	тем лишь исключением, что вместо списка создает объект xrange. 
#	Производит те же элементы, что и range(), но не сохраняет их. 
#	Преимущества использования xrange() вместо range() заметны лишь 
#	при при работе с огромным количеством элементов или в ситуации, 
#	когда сами по себе созданные элементы нами не используются, нам 
#	не нужно изменять их или порядок в котором они расположены.

#	Например, вот такая команда приведет к MemoryError

	my_list = range(999999999)
	
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	MemoryError
 
#	В то время, как xrange() создаст нужный объект.

	my_list = xrange(999999999)