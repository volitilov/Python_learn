Exception :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Исключения (exceptions) - ещё один тип данных в python. Исключения 
# необходимы для того, чтобы сообщать программисту об ошибках. 
# Программисты могут создавать собственные исключения.

# документация на английском:
# https://docs.python.org/3/library/exceptions.html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Для обработки исключений предназначена инструкция try. Формат 
# инструкции:

try:
	# Блок, в котором перехватываются исключения
except Исключение as Объект исключения:
	# Блок, выполняемый при возникновении исключения
else:
	# Блок, выполняемый, если исключение не возникло
finally:
	# Блок, выполняемый в лю6ом случае




# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Для возбуждения пользовательских исключений предназначены две 
# инструкции:

raise
# Инструкция raise возбуждает заданное исключение. Она имеет несколько 
# вариантов фор­мата:
	raise <Экземпляр класса>:
	# указывается экземпляр класса возбуждае­мого исключения. При 
	# создании экземпляра можно передать данные конструктору класса.
	# Эти данные будут доступны через второй параметр в инструкции 
	# except.
	raise <Название класса>:
	# задается объект клас­са, а не экземпляр. 
	raise <Экземпляр или название класса> from <Объект исключения>:
	# в первом параметре задается экземпляр класса или просто название 
	# класса, а во втором параметре указывается объект исключения.
	# В этом случае объект исключения сохраняется в атрибуте __cause__. 
	# При обработке вло­женных исключений эти данные используются для 
	# вывода информации не только о послед­нем исключении, но и о 
	# первоначальном исключении.
	raise:
	# позволяет повторно возбудить последнее исключение и обычно 
	# применяется в коде. следующем за инструкцией except.


assert
# возбуждает искточение AssertionError, если логическое выражение
# возвращает значение False.




# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

BaseException
# базовое исключение, от которого берут начало все остальные.

	SystemExit
	# исключение, порождаемое функцией sys.exit при выходе из программы.

	KeyboardInterrupt
	# порождается при прерывании программы пользователем (обычно 
	# сочетанием клавиш Ctrl+C).

	GeneratorExit
	# порождается при вызове метода close объекта generator.

	Exception
	# тут уже заканчиваются полностью системные исключения (которые лучше 
	# не трогать) и начинаются обыкновенные, с которыми можно работать.

		StopIteration
		# порождается встроенной функцией next, если в итераторе больше 
		# нет элементов.

		StopAsyncIteration
		# Используется для остановки асинхронного прохода. Это исключение 
		# обрабатывается конструкцией async for и должно возбуждаться 
		# методом __anext__() асинхронного итератора для индикации 
		# остановки итерирования.

		ArithmeticError
		# арифметическая ошибка.

			FloatingPointError
			# порождается при неудачном выполнении операции с плавающей 
			# запятой.

			OverflowError
			# возникает, когда результат арифметической операции слишком 
			# велик для представления. Не появляется при обычной работе с 
			# целыми числами (так как python поддерживает длинные числа), 
			# но может возникать в некоторых других случаях.

			ZeroDivisionError
			# деление на ноль.

		AssertionError
		# выражение в функции assert ложно.

		AttributeError
		# объект не имеет данного атрибута (значения или метода).

		BufferError
		# операция, связанная с буфером, не может быть выполнена.

		EOFError
		# функция наткнулась на конец файла и не смогла прочитать то, 
		# что хотела.

		ImportError
		# не удалось импортирование модуля или его атрибута.

			ModuleNotFoundError
			# создается при импорте, когда не может найти модуль.

		LookupError
		# некорректный индекс или ключ.

			IndexError
			# индекс не входит в диапазон элементов.

			KeyError
			# несуществующий ключ (в словаре, множестве или другом 
			# объекте).

		MemoryError
		# недостаточно памяти.

		NameError
		# не найдено переменной с таким именем.

			UnboundLocalError
			# сделана ссылка на локальную переменную в функции, но 
			# переменная не определена ранее.

		OSError
		# ошибка, связанная с системой.

			BlockingIOError
			# исключение, возникающее в случаях блокировки ввода-вывода.

			ChildProcessError
			# неудача при операции с дочерним процессом.

			ConnectionError
			# базовый класс для исключений, связанных с подключениями.

				BrokenPipeError
				# исключение возбуждается в случае попытки записи в канал 
				# (pipe), когда второй его конец закрыт, а также при 
				# попытке записи в сокет, более недоступный для записи.	

				ConnectionAbortedError
				# исключение, возникающее в случае завершения узлом 
				# соединения

				ConnectionRefusedError
				# исключение, возникающее в случае отказа узла в 
				# попытке соединения

				ConnectionResetError
				# исключение, возникающее в случае сброса узлом 
				# соединения

			FileExistsError
			# попытка создания файла или директории, которая уже 
			# существует.

			FileNotFoundError
			# файл или директория не существует.

			InterruptedError
			# системный вызов прерван входящим сигналом.

			IsADirectoryError
			# ожидался файл, но это директория.

			NotADirectoryError
			# ожидалась директория, но это файл.

			PermissionError
			# не хватает прав доступа.

			ProcessLookupError
			# указанного процесса не существует.

			TimeoutError
			# закончилось время ожидания.

		ReferenceError
		# попытка доступа к атрибуту со слабой ссылкой.

		RuntimeError
		# возникает, когда исключение не попадает ни под одну из других 
		# категорий.

			NotImplementedError
			# возникает, когда абстрактные методы класса требуют 
			# переопределения в дочерних классах.

			RecursionError
			# Поднимается, когда интерпретатор обнаруживает что 
			# достигнут предел для рекурсивных вызовов

		SyntaxError
		# синтаксическая ошибка.

			IndentationError
			# неправильные отступы.

				TabError
				# смешивание в отступах табуляции и пробелов.

		SystemError
		# внутренняя ошибка.

		TypeError
		# операция применена к объекту несоответствующего типа.

		ValueError
		# функция получает аргумент правильного типа, но некорректного 
		# значения.

			UnicodeError
			# ошибка, связанная с кодированием / раскодированием unicode в 
			# строках.

				UnicodeDecodeError
				# исключение, связанное с декодированием unicode.

				UnicodeEncodeError
				# исключение, связанное с кодированием unicode.

				UnicodeTranslateError
				# исключение, связанное с переводом unicode.

		Warning
		# Базовый класс для исключений-предупреждений.

			DeprecationWarning
			# Эту категорию обычно используют для указания на то, что некая 
			# часть функциональности морально устарела (возможно ей на смену 
			# пришла более совершенная) и не рекомендуется к использованию.

			PendingDeprecationWarning
			# Категория предупреждений о функциональности, которая вскоре 
			# должна стать нежелательной к использованию.
			
			RuntimeWarning
			# Категоря может быть использована для обозначения сомнительного 
			# поведения приложения, например, если код выявил вероятные 
			# погрешности в вычислениях

			SyntaxWarning
			# Категория используется в случаях, когда замечены вероятные 
			# синтаксические ошибки.

			UserWarning
			# Может использоваться пользователями в качестве базового класса 
			# для создания собственных иерархий предупреждений.
			
			FutureWarning
			# Предупреждения данной категории призваны оповещать о грядущих 
			# [семантических] изменениях.
			
			ImportWarning
			# Предупреждения данной категории могут использоваться, например, 
			# в случаях внесения изменений в систему импорта при помощи 
			# перехватчиков (хуков).
			
			UnicodeWarning
			# Предупреждения, связанные с возможными проблемами при работе 
			# с Юникод.
			
			BytesWarning
			# Данная категория предупреждений используется в случаях 
			# возможных ошибок при работе с бйтами (bytes и bytearray).

			ResourceWarning
			# Примером использования данной категории предупреждений можут 
			# служить указание на необходимость закрытия сокета, что 
			# необходимо для высвобождения ресурсов.