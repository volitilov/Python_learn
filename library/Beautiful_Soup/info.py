pip3 install beautifulsoup4

import bs4

# предназначен для извлечения информации из HTML-страниц

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# bs4.BeautifulSoup(res.text)
bs = bs4.BeautifulSoup('example.html')
# получение объекта BeautifulSoup, для того чтобы можно было 
# использовать его методы для поиска отдельных частей HTML-документа

els = bs.select('p #author')
# возвращает список объектов Tag, предоставляющий в BeautifulSoup
# HTML-элементы.

els[0].getText() # 'example text'
# получение содержание первого тэга

str(els[0]) # '<p id="author">example text</p>'
# получение тэга

els[0].attrs # {'id': 'author'}
# получение атрибутов тега в виде словаря

els.get('id') # 'author'
# получение значений атрибутов