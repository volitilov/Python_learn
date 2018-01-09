_CharacterStyle :::::::::::::::::::::::::::::::::::::::::::::::

# Стиль символа применяется к объекту Run и в основном 
# обеспечивает форматирование на уровне символа через объект 
# Font в свойстве шрифта.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# получение объекта styles
doc = Document(docx_file)
paragraph = doc.paragraphs[0]
run_obj = paragraph.runs[0]
_character_style = run_obj._character_style

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

base_style
#

builtin
#

delete()
#

font
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
