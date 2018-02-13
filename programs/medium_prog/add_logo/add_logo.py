# add_logo.py
# изменяет размеры и добавляет изображения в верхний правый угол 
# для изображений расположенных в коталоге imgs

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os
from PIL import Image

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# водяной знак
EX_IMG = 'popular2.png'

# размеры исходных изображений
width, height = 300, 300

# полный путь к папке с изображениями
imgs = os.path.abspath('imgs')

logo_img = Image.open(EX_IMG)

# координаты расположения водянного знака
x_point = width - logo_img.size[0]
y_point = 0


# перебор изображений в папке imgs
for num, infile in enumerate(os.listdir(imgs)):
	# получаю расширение файла
	_, ext = os.path.splitext(infile)

	file = imgs + '/' + infile

	# конвертирую изображения для добавления alfa составляющей
	im = Image.open(file).convert("RGBA")
	
	# подгонка размера
	im.thumbnail((width, height))
	
	# добавляю логотип
	# im.paste(logo_img, (x_point, y_point))
	im.alpha_composite(logo_img, dest=(x_point, y_point))

	# сохраняю изменения
	os.makedirs('imgs2', exist_ok=True)
	im.save('imgs2/' + str(num+1) + ".thumbnail" + ext)
