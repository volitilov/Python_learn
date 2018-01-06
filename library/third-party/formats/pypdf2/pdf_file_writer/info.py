from PyPDF2.PdfFileWriter import *

PdfFileWriter()
# создаёт объект PdfFileWriter, знвчение которое представляет 
# PDF-документ в Python, при этом фактический PDF-файл не 
# создаётся 

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

addAttachment(fname, fdata)
#

addBlankPage(width=None, height=None)
#

addBookmark(title, pagenum, parent=None, color=None, 
	bold=False, italic=False, fit='/Fit', *args)
#

addJS(javascript)
#

addLink(pagenum, pagedest, rect, border=None, fit='/Fit', *args)
#

addMetadata(infos)
#

addPage(page)
# добавление станицы

appendPagesFromReader(reader, after_page_append=None)
#

cloneDocumentFromReader(reader, after_page_append=None)
#

cloneReaderDocumentRoot(reader)
#

encrypt(user_pwd, owner_pwd=None, use_128bit=True)
# шифрует паролем PDF-документ. PDF может иметь пароль 
# пользователя (для чтения), и пароль владельца 
# (позволяющий устанавливать разрешения для вывода 
# документа на печать, снабжения его комментариями, 
# извлечение текста, а также предоставление других прав)

getNumPages()
#

getPage(pageNumber)
#

getPageLayout()
#

getPageMode()
#

insertBlankPage(width=None, height=None, index=0)
#

insertPage(page, index=0)
#

pageLayout
#

pageMode
#

removeImages(ignoreByteStringObject=False)
#

removeLinks()
#

removeText(ignoreByteStringObject=False)
#

setPageLayout(layout)
#

setPageMode(mode)
#

updatePageFormFieldValues(page, fields)
#

write(stream)
# создаёт фактический PDF-файл объекта PdfFileWriter