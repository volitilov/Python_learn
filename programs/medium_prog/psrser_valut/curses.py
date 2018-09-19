#!/home/x/Works/.VENVS/LEARN/bin/python3

# парсит данные по курсам валют в РБ и формирует в удобочитаемый вид,
# затем отправляет эти данные как системное уведомление

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import requests, os
from bs4 import BeautifulSoup

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def get_html():
	url = 'https://finance.tut.by/kurs/minsk/'
	r = requests.get(url)
	return r.text


def create_courseRate_list(html):
	bs = BeautifulSoup(html, 'html.parser')
	list_currencies = bs.select('.rates-table tr')[1:]

	currencies = []
	for i in list_currencies:
		if i.td.a != None:
			currencies.append({
				'name': i.td.a.string,
				'value': i.select_one('.b-course p').string
			})

	return currencies[:10]


def create_format_message(currencies):
	body = '\n'
	for i in currencies:
		body += '{:.<30} {} \n'.format(i['name'], i['value'])
	return body


def show_message(message_body):
	title = 'Курсы валют в РБ на сегодня'
	body = message_body
	os.system('sudo notify-send "{}" "{}"'.format(title, body))



def main():
	html = get_html()
	# получаю html

	currencies = create_courseRate_list(html)
	# получаю список валют с их значениями
	
	message_body = create_format_message(currencies)
	# получаю форматированый текст
	
	show_message(message_body)
	# распечатываю данные

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	main()

