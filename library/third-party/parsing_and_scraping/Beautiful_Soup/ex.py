# import requests
from bs4 import BeautifulSoup

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

BeautifulSoup("<a></p>", "html.parser")
# <a></a>

BeautifulSoup("<a></p>", "html5lib")
# <html><head></head><body><a><p></p></a></body></html>

BeautifulSoup("<a></p>", "lxml")
# <html><body><a></a></body></html>

BeautifulSoup("<a><b /></a>", "xml")
# <?xml version="1.0" encoding="utf-8"?>
# <a><b/></a>

BeautifulSoup("<a><b /></a>")
# <html><head></head><body><a><b></b></a></body></html>



# res = requests.get('https://vk.com/volitilov')

# try:
# 	res.raise_for_status()
# 	with open('ex.html', 'wb') as file:
# 		for chunk in res.iter_content(100000):
# 			file.write(chunk)
# except Exception as exc:
# 	print('Ошибка: {}'.format(exc))


with open('example.html') as file:
	soup = BeautifulSoup(file.read(), 'html.parser')
	# print(soup.prettify())
	# print(soup.title)
	# print(soup.title.string)
	# print(soup.title.parent.name)
	# print(soup.a)
	# print(soup.a['class'])
	# print(soup.find_all('a'))
	# print(soup.find(id='img_ex'))
	# for link in soup.find_all('a'):
	# 	print(link.get('href'))

	# print(soup.get_text())

	# tag = soup.img
	# tag.name = 'a'
	# tag['id'] = 'brand'
	# tag['class'] = ['brand_image', 'image']
	# print(tag)
	# tag.name = 'img'
	# print(tag)
	# del tag['id']
	# print(tag)
	# print(tag.name)
	# print(tag['class'])
	# print(tag.attrs)

	# print(soup.img['class'])
	# print(soup.img.attrs)

	# print(soup.span.string)
	# soup.span.string.replace_with('experement_text')
	# print(soup.span.string)

	btn = soup.find_all(attrs={"type": "button"})
	print(btn)