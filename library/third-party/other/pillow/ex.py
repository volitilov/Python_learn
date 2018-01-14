from PIL import (ImageColor, Image, ImageDraw, ImageFont)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# i = ImageColor.getcolor('red', 'RGBA')
# print(i)

# i = Image.open('qr.png')
# print(i.format, i.size, i.mode, i.filename, 
# 	i.format_description)

# i = Image.new('RGBA', (100, 100), 'green')
# i2 = Image.new('RGBA', (20, 20), 'red')
# i.save('ex_image.png')
# i2.save('ex_image2.png')

# i = Image.open('ex_image.png')
# i2 = Image.open('ex_image2.png')
# i.paste(i2, (40,40))
# i.save('i3.png')


# i = Image.open('qr.png')
# i.show()

# with Image.open('ex_image.png') as i:
# 	width, height = i.size
# 	new_i = i.resize((int(width/2), int(height/2)))
# 	new_i.save('i3.png')


# with Image.new('RGBA', (200, 200)) as i:
# 	width, height = i.size
# 	for x in range(0, width, 2):
# 		for y in range(0, height):
# 			i.putpixel((x, y), (0, 0, 0, 255))
# 	i.save('i3.png')

with Image.new('RGBA', (300, 300)) as image:
	draw = ImageDraw.Draw(image)
	draw.line(((0, 0), (150, 300)), fill=(255, 0, 0), width=20)
	# красная линия
	draw.arc(((150, 150), (250, 250)), 45, 210, fill=(0, 255, 0))
	# зелёная дуга
	draw.rectangle(((50, 50), (150, 150)), fill=(0, 0, 255))
	# синий квадрат

	font = ImageFont.truetype("data/kaligrafica_allfont_ru.ttf", 32)
	draw.text((200, 200), 'Hello world!', (255, 255, 0), font=font)
	# жёлтый текст
	image = image.rotate(90)
	# поворот на 90 градусов
	image.save('sample.png')