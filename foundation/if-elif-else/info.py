# 	////////////////////////////////////////////////////////////
# 	Инструкция if-elif-else ////////////////////////////////////

#	Условная инструкция if-elif-else (её ещё иногда называют 
#	оператором ветвления) - основной инструмент выбора в Python. 
#	Проще говоря, она выбирает, какое действие следует выполнить, 
#	в зависимости от значения переменных в момент проверки условия.

#	Синтаксис инструкции if ....................................

#	Сначала записывается часть if с условным выражением, далее 
#	могут следовать одна или более необязательных частей elif, и 
#	необязательная часть else. Общая форма записи условной 
#	инструкции if выглядит следующим образом:

	if test1:
    	state1
	elif test2:
    	state2
	else:
    	state3

#	Конструкция с несколькими elif может также служить отличной 
#	заменой конструкции switch - case в других языках 
#	программирования.

#	Проверка истинности в Python ...............................

#	- Любое число, не равное 0, или непустой объект - истина.
#	- Числа, равные 0, пустые объекты и значение None - ложь
#	- Операции сравнения применяются к структурам данных рекурсивно
#	- Операции сравнения возвращают True или False

#	- Логические операторы and и or возвращают истинный или ложный 
#	  объект-операнд

#	Логические операторы .......................................

	X and Y		# Истина, если оба значения X и Y истинны.

	X or Y		# Истина, если хотя бы одно из значений X или Y 
				# истинно.

	not X		# Истина, если X ложно.


#	Трехместное выражение if/else ..............................

	if X:
    	A = Y
	else:
    	A = Z

#	короткая, но, тем не менее, занимает целых 4 строки. 
#	Специально для таких случаев и было придумано выражение if/else:

	A = Y if X else Z