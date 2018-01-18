# mouse_now.py
# отображает текущую позицию указателя мыши

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import pyautogui as pg

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

print('Для выхода нажмите клавиши <Ctrl+C>')

try:
	while True:
		# TODO: получить и вывести координаты указателя мыши
		x, y = pg.position()
		position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
		print(position_str, end='')
		print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
	print('\nГотово.')