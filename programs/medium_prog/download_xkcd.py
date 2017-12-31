#!/usr/bin/python3

# download_xkcd.py
# загружает заданное кол-во комиксов с сайта https://xkcd.com
# с исполшьзованием нескольких потоков выполнения

# Использование: ./download_xkcd.py 10

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import requests, bs4, sys, os, subprocess
from threading import Thread
from collections import deque

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def search_img_urls(count):
	img_links = deque()
	template_url = 'https://xkcd.com/'
	self_url =  template_url
	count = int(count)

	while count:
		# запрос страницы
		res = requests.get(self_url)
		try:
			res.raise_for_status()
			soup = bs4.BeautifulSoup(res.text, 'html.parser')
			# получение изображения на страницы
			img = soup.select('#comic img')[0]
			# получение ссылки изображения
			img_href = 'https:' + img['src']
			# получение название файла
			img_basename = os.path.basename(img_href)

			# получение ссылки кнопки prev
			prev_url = soup.find(rel='prev').get('href')
			# создание полноценного адреса предедущий страницы
			self_url = template_url + prev_url

			obj = {
				'name': img_basename,
				'url': img_href
			}
			
			img_links.append(obj)

			count -= 1


		except Exception as exc:
			print('Ошибка: {}'.format(exc))

	return img_links




class DownloadThread(Thread):
	"""Пример многопоточной загрузки файлов из интернета"""
	def __init__(self, img):
		Thread.__init__(self)
		self.url = img['url']
		self.name = img['name']

	def run(self):
		"""запуск патока"""
		res = requests.get(self.url)
		
		try:
			res.raise_for_status()

			# создание пути для изображения
			file_path = os.path.join('xkcd', self.name)

			# копирование файла
			with open(file_path, 'wb') as file:
				for chunk in res.iter_content(100000):
					file.write(chunk)
				subprocess.call(['echo', '-e', 
					'Загруженно: \e[35m{}\e[0m'.format(self.name)])
			print()
		except Exception as exc:
			print('Возникла проблема: {}'.format(exc))




# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if len(sys.argv) == 2 and type(int(sys.argv[1])).__name__ == 'int':
	os.makedirs('xkcd', exist_ok=True)
	ths = []

	img_links = search_img_urls(sys.argv[1])

	while img_links:
		img = img_links.popleft()
		thread = DownloadThread(img)
		ths.append(thread)
		thread.start()

	for th in ths:
		th.join()

	print('\nГотово.\n')

else:
	print('Использование: ./download_xkcd.py 10')