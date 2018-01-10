from PyPDF2.PdfFileMerger import *

# Инициализирует объект PdfFileMerger. PdfFileMerger объединяет 
# несколько PDF-файлов в один PDF-файл. Он может конкатенировать, 
# нарезать, вставить или любую комбинацию из вышеперечисленного

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PdfFileMerger(
	strict=True
	# Определяет, следует ли предупреждать пользователя обо всех 
	# проблемах, а также приводит к тому, что некоторые 
	# исправляемые проблемы являются фатальными. По умолчанию 
	# используется значение True.
)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

addBookmark(title, pagenum, parent=None)
#

addMetadata(infos)
#

addNamedDestination(title, pagenum)
#

append(fileobj, bookmark=None, pages=None, import_bookmarks=True)
#

close()
#

merge(position, fileobj, bookmark=None, pages=None, import_bookmarks=True)
#

setPageLayout(layout)
#

setPageMode(mode)
#

write(fileobj)
#

