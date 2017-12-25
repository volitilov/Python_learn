#!/usr/bin/python3

# stopwatch.py 
# простая программа-хронометр

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# отображение инструкции по использованию программы
print('	\nЧтобы начать отсчёт, нажмите клавишу ENTER. Впоследствии \
		\nдля имитации щелчков кнопки секундомера, нажимайте клавишу \
		\nENTER. Для выхода из программы нажмите клавиши CTRL+C')

# нажатие клавиши ENTER начинает отсчет
input()
print('Отсчёт начат')

startTime = time.time()
lastTime = startTime
lapNum = 1

# отслеживание замеров
try:
	while True:
		input()
		# считает время замера
		lapTime = round(time.time() - lastTime, 2)
		# считает сумарно истёкшее время
		totalTime = round(time.time() - startTime, 2)
		print('Замер {}: {} ({})'.format(lapNum, totalTime, lapTime), end='')
		lapNum += 1
		# переустановить время последнего замера
		lastTime = time.time()
except KeyboardInterrupt:
	# обработать исключение <Ctrl+C>, чтобы предотвратить 
	# отображение его сообщений
	print('\nГотово.')