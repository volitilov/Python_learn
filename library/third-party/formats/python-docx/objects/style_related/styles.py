Styles ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Коллекция, обеспечивающая доступ к стилям, определенным в 
# документе. Доступ осуществляется с использованием свойства 
# Document.styles. Поддерживает доступ к len(), итерации и 
# словарный стиль по имени стиля.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# получение объекта styles
doc = Document(docx_file)
paragraph = doc.paragraphs[0]
run_obj = paragraph.runs[0]
styles = run_obj.styles

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

add_style(name, style_type, builtin=False)
#

default(style_type)
#

element
#

latent_styles
#

builtin
#

delete()
#

hidden
#

locked
#

name
#

priority
#

quick_style
#

unhide_when_used
#		