import logging

# Упращает создание и ведения журнала отчётов на основе
# подготовленных сообщений. Сообщение протоколирования
# включает описание того, когда именно программа достигла
# вызова функции протоколирования, а также список значений
# указаных переменных в данный момент времени.
# Упрощает переключение между режимами отображения и
# сокрытия сообщений протоколирования

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

logging.basicConfig(level=logging.DEBUG, 
		format='%(asctime)s - %(levelname)s - %(message)s')
# выводит сообщения в консоль
# позволяет конкретезировать, какую иммено информацию
# об объекте, и в какой именно форме
# level - отображение сообщений, начиная с этого уровня 
# критичности

logging.basicConfig(
		filename='my_log.txt',
		level=logging.DEBUG, 
		format='%(asctime)s - %(levelname)s - %(message)s')
# записывает сообщения в журнал

logging.debug(folder_name)
# вывод протоколируемой информации

logging.desable(logging.CRITICAL)
# отключает все следующие за ним инструкции протоколирования


# Уровни критичности сообщений ::::::::::::::::::::::::::::

logging.debug()	# DEBUG
# Самый низкий уровень. Используется для вывода подробных
# сведений технического характера. Обычно используется
# в процессе диагностирования проблем.

logging.info() # INFO
# Используется для записи об обычных сабытиях, происходящих
# в программе, или для потверждения нормального хода работы
# программы

logging.warning() # WARNING
# Используется для индикации потенциально опасных ситуаций,
# которые не препятствуют работе программы, но могут привести
# к этому в будущем

logging.error() # ERROR
# Используется для записи информации об ошибке, которая 
# привела к тому, чтопрограмма не смогла выполнить некоторые
# действия

logging.critical() # CRITICAL
# Наивыйсший уровень. Используется для индикации, фатальных
# ошибок которые привели или могут привести к полному 
# прекращению работы программы

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::