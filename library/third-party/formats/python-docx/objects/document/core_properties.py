CoreProperties :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Каждый объект Document обеспечивает доступ к объекту CoreProperties 
# через свой атрибут core_properties. Объект CoreProperties 
# предоставляет доступ для чтения/записи к так называемым основным 
# свойствам документа. К основным свойствам относятся автор, категория, 
# комментарии, content_status, созданные, идентификатор, ключевые слова, 
# язык, last_modified_by, last_printed, измененный, ревизия, тема, 
# название и версия.

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

doc = Document(docx_file)
core_properties = doc.core_properties

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

author
#

category
#

comments
#

content_status
#

created
#

identifier
#

keywords
#

language
#

last_modified_by
#

last_printed
#

modified
#

revision
#

subject
#

title
#

version
#
