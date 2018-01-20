#!VENV/bin/python3

# mouse_now.py
# отображает:
# - текущую позицию указателя мыши
# - RGBA цвет пикселя находящегося под указателем

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import pyautogui as pg

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

print('Для выхода нажмите клавиши <Ctrl+C>')

try:
	while True:
		# получение и вывод координат указателя мыши
		x, y = pg.position()
		position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
		pixel_color = pg.screenshot().getpixel((x, y))

		position_str += ' RGBA: (' + str(pixel_color[0]).rjust(3)
		position_str += ', ' + str(pixel_color[1]).rjust(3)
		position_str += ', ' + str(pixel_color[2]).rjust(3) + ')'

		print(position_str, end='')
		print('\b' * len(position_str), end='', flush=True)

		# получение RGBA цвета пикселя находящегося под указателем
except KeyboardInterrupt:
	print('\nГотово.')