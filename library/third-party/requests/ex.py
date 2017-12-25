import requests as req

# ::::::::::::::::::::::::::::::::::::::::

# получаем веб-страницу
res = req.get('https://api.github.com/user', auth=('volitilov@gmail.com', 'Stas6709'))


try:
	res.raise_for_status()
	# записываем в файл полученные данные
	# with open('ex.html', 'wb') as file:
	# 	for chunk in res.iter_content(100000):
	# 		file.write(chunk)
	# print('Ok')
except Exception as exc:
	print('Возникла проблема: {}'.format(exc))



print(res.headers['content-type'])
# text/json; charset=utf-8

print(res.status_code)
# 200

print(res.json())
# {'starred_url': 'h...