from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

# :::::::::::::::::::::::::::::::::::::::::::::::

# добавляем путь к скачаным драйверам
# browser = webdriver.Chrome('/home/py/Draivers/browsers/chromedriver')

# use with Chrome
browser = webdriver.Chrome(ChromeDriverManager().install())

# use with Firefox
# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# use with Edge:
# driver = webdriver.Edge(EdgeDriverManager().install())

# use with IE
# driver = webdriver.Ie(IEDriverManager().install())

# use with PhantomJS:
# driver = webdriver.PhantomJS(PhantomJsDriverManager().install())


browser.get('https://vk.com/volitilov')

try:
	el_email = br.find_element_by_id('quick_email')
	el_email.click()
	el_email.send_keys('example@mail.ru')

	el_pass = br.find_element_by_id('quick_pass')
	el_pass.click()
	el_pass.send_keys('ExPassword_QWE_123')

	# btn_login = br.find_element_by_id('quick_login_button')
	el_pass.submit()

except Exception as exc:
	print('Error: {}'.format(exc))



try:
	el = br.find_element_by_tag_name('html')
	# прокрутка в конец
	el.send_keys(Keys.END)
	# прокрутка в начало
	el.send_keys(Keys.HOME)

except Exception as exc:
	print('Error: {}'.format(exc))