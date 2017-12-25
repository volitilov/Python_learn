#!/usr/bin/python3

# quick_weather.py
# выводит прогноз погоды для заданного населённого пункта

# Использование: ./quick_weather.py 'Vitebsk'

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import json, sys, os, requests
from pprint import pprint
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if len(sys.argv) < 2 or len(sys.argv) > 2:
	print('Использование: ./quick_weather.py "Vitebsk"')

if len(sys.argv) == 2:
	# получение населённого пункта
	location = str(sys.argv[1])
	url = 'http://api.openweathermap.org/data/2.5/forecast?'
	api_key = '524901&APPID=61a5548c0d359dc2f0b0523baee1a47c'
	# авторизация
	url += 'id={}'.format(api_key)
	# формирование ссылки запроса
	url += '&q={},by&cnt=3'.format(location)

	# загрузка JSON-данных из API сайта OpenWeatherMap.org
	response = requests.get(url)
	response.raise_for_status()
	# преобразование данных из JSON в Python
	weather_data = json.loads(response.text)
	
	# вывод полученных данных
	for w_d in weather_data['list']:
		print()
		print(w_d['dt_txt'])
		temp = int(w_d['main']['temp']) / -272.15
		print(round(temp))
		print(w_d['weather'][0]['description'])
		print()