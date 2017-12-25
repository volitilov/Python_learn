#!/usr/bin/python3

# lucky.py
# принимает запросы на поиск в google из командной строки
# и открывает несколько результатов во вкладках

# Использование: ./lucky.py 'volitilov'

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 

import webbrowser, requests, sys, bs4

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def search_urls(arg, count):
	url = 'https://www.google.com/search?q='
	res = requests.get(url+arg)
	list_urls = []

	try:
		res.raise_for_status()

		# извлечение несколько найденных ссылок
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		for link in soup.select('.r a')[:count]:
			list_urls.append(link.get('href'))

		return list_urls
	except Exception as exc:
		print('Ошибка: {}'.format(exc))



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if len(sys.argv) == 2 and sys.argv[1] != None:
	urls = search_urls(sys.argv[1], 3)
	# открытие ссылок в браузере
	for url in urls:
		template_url = 'https://www.google.com' + url
		webbrowser.open(template_url)

else:
	print('Использование: ./lucky.py "ex_search" ')