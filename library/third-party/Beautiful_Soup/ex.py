import requests
from bs4 import BeautifulSoup

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# res = requests.get('https://vk.com/volitilov')

# try:
# 	res.raise_for_status()
# 	with open('ex.html', 'wb') as file:
# 		for chunk in res.iter_content(100000):
# 			file.write(chunk)
# except Exception as exc:
# 	print('Ошибка: {}'.format(exc))


with open('ex.html') as file:
	soup = BeautifulSoup(file.read(), 'html.parser')
	# print(soup.prettify())
	
	# print(soup.title)
	# <title>Вячеслав Волитилов</title>

	# print(soup.title.string)
	# Вячеслав Волитилов

	# print(soup.title.parent.name)
	# head

	# print(soup.a)
	# <a accesskey="*" class="header__left hb_wrap mhb_home mhb_vkhome" href="/">
	# 	<div class="hb_btn mhi_home mhi_vkhome"> </div>
	# </a>

	# print(soup.a['class'])
	# ['header__left', 'hb_wrap', 'mhb_home', 'mhb_vkhome']

	# print(soup.find_all('a'))
	# [<a class="post__anchor anchor" name="post115067466_719"></a>, 
	#	<a href="/volitilov">
	#		<img class="wi_img" src="https://pp.userapi.com/c840227/v840227446/49fb3/QjMvyfzJU8Q.jpg"/>
	# 	</a>
	# ]

	# print(soup.find(id='img_ex'))
	# <img class="wi_img" id="img_ex" src="ex.jpg"/>

	# for link in soup.find_all('a'):
	# 	print(link.get('href'))
		# None
		# /volitilov

	# print(soup.get_text())
	# Вячеслав Волитилов

	tag = soup.img
	print(tag.name) # img
	print(tag['class']) # ['wi_img']
	print(tag.attrs) # {'id': 'img_ex', 'src': 'ex.jpg', 'class': ['wi_img']}
