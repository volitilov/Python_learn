#!/usr/bin/python3

# work_tbl.py
# ведёт учёт времени прихода и ухода сотрудников

# Использование:
# Пришёл: ./work_tbl.py start_work
# Ушёл: ./work_tbl.py stop_work
# Просмотр: ./work_tbl.py [Фамилия] [дата](2017.12.13)
# после того, как программа стартует вводите фамилию
# сатрудника и жмёте ENTER.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import shelve, datetime, os, sys

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class User:
	def __init__(self, name):
		self.name = name
		self.work_days = []

	# поиск рабочего дня, если сотрудник работал в 
	# запрвшиваемый день, то функция вернёт объект 
	# рабочего дня, если нет то None 
	def view_works_day(self, work_day):
		for day in self.work_days:
			if day['date'] == work_day:
				return day

	def __str__(self):
		return self.name


# учёт сотрудников прихода на работу
def start_work():
	db = shelve.open('tbl')
	tbl = db['tbl']
	flag = False

	try:
		print('\nПрограмма учёта прихода сотрудников. \
			\nДля выхода из программы нажмите <Ctrl+C>\n')
		while True:
			name = input('Введите фамилию: ')
			for user in tbl:
				# проверка чтобы человек "не прошёл" два раза
				if user.name == name:
					os.system("echo 'Сотрудник:' \
					'\e[92m{}\e[0m' 'уже пришёл.'".format(name))
					flag = True
					break
			# запись сотрудника в базу
			if flag == False:
				# получение даты и времени прихода
				start = datetime.datetime.now()
				user = User(name)

				# рабочий день
				work_days_obj = {
					# дата рабочего дня
					'date': start.date().strftime('%Y.%m.%d'),
					# время начала работы
					'start_work': start.time().strftime('%H:%M:%S')
				}
				# вношу рабочий день в список рабочих дней
				# сотрудника
				user.work_days.append(work_days_obj)

				# запись в базу прихода сотрудников
				tbl.append(user)
				db['tbl'] = tbl
		
	# обработать исключение <Ctrl+C>, чтобы предотвратить 
	# отображение его сообщений
	except KeyboardInterrupt:
		print('\nГотово.\n')

	db.close()


# учёт сотрудников ухода с работы
def stop_work():
	db = shelve.open('tbl')
	tbl = db['tbl']
	flag = False

	try:
		print('\nПрограмма учёта ухода сотрудников. \
			\nДля выхода из программы нажмите <Ctrl+C>\n')
		while True:
			name = input('Введите фамилию: ')
			for user in tbl:
				if user.name == name:
					# получение даты и время конца рабочего дня
					stop = datetime.datetime.now()
					# получение даты
					now_day = stop.date().strftime('%Y.%m.%d')

					# получение объекта сегоднешнего рабочего дня 
					work_day = user.view_works_day(now_day)
					# получение времени конца рабочего дня
					stop_time = stop.time().strftime('%H:%M:%S')
					# запись в рабочий день время оканчание работы
					work_day['stop_work'] = stop_time

					db['tbl'] = tbl
					flag = True
					break

			if flag == False:
				os.system("echo 'Фамилия:' \
					'\e[92m{}\e[0m' 'не найдена.'".format(name))

	# обработать исключение <Ctrl+C>, чтобы предотвратить 
	# отображение его сообщений
	except KeyboardInterrupt:
		print('\nГотово.\n')

	db.close()


# просмотр информации и сотруднике
def view_user_info(name, date):
	db = shelve.open('tbl')
	user_flag = False
	date_flag = False

	# tbl = db['tbl']
	# tbl.clear()
	# db['tbl'] = tbl
	for user in db['tbl']:
		if user.name == name:
			# получение рабочего дня по дате
			work_day = user.view_works_day(date)
			user_flag = True
			if work_day:
				date_flag = True
				os.system("echo '\n\e[92m{}\e[0m' '{}'\
					".format(user, work_day['date']))
				os.system("echo '- Пришёл:' '\e[92m{}\e[0m' \
					".format(work_day['start_work']))
				os.system("echo '- Ушёл:' '\e[92m{}\e[0m\n' \
					".format(work_day['stop_work']))

	if user_flag == False:
		print('Пользователя: {} - нет в базе.'.format(name))

	if date_flag == False:
		print('Дата: {} - у работника {} отсутствует.'.format(date, name))

	db.close()

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if len(sys.argv) > 1 and sys.argv[1].lower() == 'start_work':
	start_work()

elif len(sys.argv) > 1 and sys.argv[1].lower() == 'stop_work': 
	stop_work()

elif len(sys.argv) > 2: 
	view_user_info(sys.argv[1], sys.argv[2])

else:
	os.system("echo '\nДобро пожаловать в программу учёта:' \
				'\e[92m[work_tbl]\e[0m\n'")
	print('Программа ведёт учёт прихода и ухода сотрудников')
	print('Пользование программой: \
		\n- Пришёл: ./work_tbl.py start_work \
		\n- Ушёл: ./work_tbl.py stop_work \
		\n- Просмотр: 	./work_tbl.py "Волитилов" "21.07.2017" "start_work" \
		\n 		./work_tbl.py "Волитилов" "2017.12.13" "stop_work" \
		\n- далее следуйте инструкциям...\n')
