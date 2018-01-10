from PyPDF2.PdfFileReader import *

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PdfFileReader(
	stream, 
	# путь к файлу или объект представляющий файл
	strict=True, 
	# определяет, следует ли предупреждать пользователя обо всех 
	# проблемах. По умалчанию True
	warndest=None,
	# Назначение для протоколирования предупреждений (по умолчанию 
	# sys.stderr)
	overwriteWarnings=True
	# Определяет, следует ли переопределять модуль warnings.py 
	# Python с пользовательской реализацией (по умолчанию - True)
)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

decrypt(password)
# расшифровывает объект PdfFileReader.

documentInfo
#

getDestinationPageNumber(destination)
#

getDocumentInfo()
#

getFields(tree=None, retval=None, fileobj=None)
#

getFormTextFields()
#

getNamedDestinations(tree=None, retval=None)
#

getNumPages()
#

getOutlines(node=None, outlines=None)
#

getPage(pageNumber)
# получить объект страницы, передав номер интересуюшей 
# страницы
	extractText()
	# возвратит строку содержащую текст страницы
	mergePage(other_page)
	# налаживает одну страницу на другую

getPageLayout()
#

getPageMode()
#

getPageNumber(page)
#

getXmpMetadata()
#

isEncrypted
# проверка, зашифровани ли файл. Если True то да.

namedDestinations
#

numPages
# полное кол-во страниц в документе

outlines
#

pageLayout
#

pageMode
#

pages
#

xmpMetadata
#