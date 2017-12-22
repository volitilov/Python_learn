SELENIUM ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Selenium -- это инструмент для автоматизированного управления 
# браузерами. Наиболее популярной областью применения Selenium 
# является автоматизация тестирования веб-приложений. Однако 
# при помощи Selenium можно (и даже нужно!) автоматизировать 
# любые другие рутинные действия, выполняемые через браузер.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# документация на английском: http://selenium-python.readthedocs.io/
# документация на русском: https://habrahabr.ru/post/248559/

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# установка
pip3 install selenium

# менеджер для управления драйверами
pip3 install webdriver_manager

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from selenium import webdriver

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

br = webdriver.Chrome()
# подключение к браузеру Chrome

br.get(url)
# открывает ссылку в браузере



# search elements :::::::::::::::::::::::::::::::::::::::::::::::

# find_element_*(), find_elements_*() :::::::::::::::::::::::::::
# если элементы, являющиеся объектом поиска метода, отсутствуют
# на странице, модуль selenium возбуждает исключение 
# NoSuchElementException

el = br.find_element_by_class_name(name)
br.find_elements_by_class_name(name)
# элементы, имеющий CSS класс с указаным именем

br.find_element_by_css_selector(selector)
br.find_elements_by_css_selector(selector)
# элементы, соответствующие указанному селектору CSS

br.find_element_by_id(id)
br.find_elements_by_id(id)
# элементы, соответствующие указанному значению атрибута id

br.find_element_by_link_text(text)
br.find_elements_by_link_text(text)
# элементы <a>, полностью совподающие с указанным текстом

br.find_element_by_partial_link_text(text)
br.find_elements_by_partial_link_text(text)
# элементы <a>, содержащие указанный текст

br.find_element_by_name(name)
br.find_elements_by_name(name)
# элементы, содержащие атребут с указанным именем

br.find_element_by_tag_name(name)
br.find_elements_by_tag_name(name)
# элементы, с указанным именем тега (регистр не учитывается);
# именам <a> и <A> будет соответствовать тег <a>

br.find_element_by_xpath("//input[@id='passwd-id']")
# элемент input, для которого определен атрибут с именем id и 
# значением passwd-id

#  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

el.tag_name
# имя тега; например, a в случае элемента <a>

el.get_attribute(name)
# значение атрибута с указанным именем для данного элемента

el.text 
# текст, содержащийся в элементе; например 'hello' в случае
# элемента <span>hello</span>

el.clear()
# удаляет текст, введённый в текстовом поле или тестовой области

el.is_displayed()
# возвращает значение True, если элемент видимый, иначе - False

el.is_enabled()
# возвращает значение True для элементов ввода, если элемент
# активизирован, иначе - False

el.is_selected()
# возвращает значение True для флажка или переключателя, если
# элемент выбран, иначе - False

el.location
# словарь с ключами 'x' и 'y' для позиции элемента на странице 



# события ::::::::::::::::::::::::::::::::::::::::::::::::::

el.click()
# вызывает нажатие левой кнопки мыши

el.send_keys(text)
# ввод текста в поля ввода

el.submit()
# вызывает отправку формы

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



# Keys :::::::::::::::::::::::::::::::::::::::::::::::::::::
from selenium.webdriver.common.keys import Keys

Keys.DOWN, Keys.UP, Keys.RIGHT, Keys.LEFT
# клавиши со стрелками

Keys.ENTER, Keys.RETURN 
# клавиши <Enter> и <Return>

Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
# клавиши <Home>, <End>, <PageDown>, <PageUp>

Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
# клавиши <Esc>, <Backspace>, <Delete>

Keys.F1, Keys.F2, ... Keys.F12
# клавиши <F1> до <F12>

Keys.TAB 
# клавиша <Tab>

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 


# Щелчки на кнопках браузера ::::::::::::::::::::::::::::::

br.back()
# щелчок по кнопке Back (Назад)

br.forward()
# щелчок по кнопке Forward (Вперёд)

br.refresh()
# щелчок по кнопке Refresh (Обновить)/ Reload (Перезагрузить)

br.quit()
# щелчок по кнопке Close Window (Закроет браузер)

br.close()
# закроет вкладку

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::



# Select :::::::::::::::::::::::::::::::::::::::::::::::::
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_name('name'))
# получаем объект select 

select.select_by_index(index)
# выделение по индексу

select.select_by_visible_text("text")
# выделение по тексту

select.select_by_value(value)
# выделение по значению

select.deselect_all()
# снимает выделение со всех тегов OPTION первого тега 
# SELECT на странице

select.all_selected_options
# список всех выделенных по умолчанию опций

options = select.options
# получения всех доступных опций

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Перетаскивание ::::::::::::::::::::::::::::::::::::::::
from selenium.webdriver import ActionChains

element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

action_chains = ActionChains(br)
#

action_chains.drag_and_drop(element, target)
# перетаскивание

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::



# НАДО ДОПИСАТЬ

# TODO: Переключение между окнами и фрэймами
# TODO: Всплывающие окна
# TODO: Навигация: история и локация
# TODO: Куки (cookies)