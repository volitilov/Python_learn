# создаю класс Thread, который скачивает параллельно файлы 
# из интернета

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from threading import Thread
import os, requests

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class DownloadThread(Thread):
	"""Пример многопоточной загрузки файлов из интернета"""
	def __init__(self, url, name):
		Thread.__init__(self)
		self.name = name
		self.url = url

	def run(self):
		"""запуск патока"""
		f_name = os.path.basename(self.url)
		res = requests.get(self.url)
		
		try:
			res.raise_for_status()
			# записываем в файл полученные данные
			with open(f_name, 'wb') as file:
				for chunk in res.iter_content(100000):
					file.write(chunk)
			msg = '{} закончил загрузку {}'.format(self.name, self.url)
			print(msg)
		except Exception as exc:
			print('Возникла проблема: {}'.format(exc))




def main(urls):
	"""запуск программы"""
	for item, url in enumerate(urls):
		name = 'Поток #{}'.format(item+1)
		thread = DownloadThread(url, name)
		thread.start()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	urls = [
		'http://www.irs.gov/pub/irs-pdf/f1040.pdf',
		'http://www.irs.gov/pub/irs-pdf/f1040a.pdf',
		'http://www.irs.gov/pub/irs-pdf/f1040ez.pdf',
		'http://www.irs.gov/pub/irs-pdf/f1040es.pdf',
		'http://www.irs.gov/pub/irs-pdf/f1040sb.pdf'
	]

	main(urls)