_TableStyle :::::::::::::::::::::::::::::::::::::::::::::::::::

# Стиль таблицы обеспечивает форматирование символов и абзацев 
# для его содержимого, а также специальные свойства 
# форматирования таблицы.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# получение объекта styles
doc = Document(docx_file)
paragraph = doc.paragraphs[0]
run_obj = paragraph.runs[0]
_paragraph_style = run_obj._table_style

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

next_paragraph_style
#

paragraph_format
#

priority
#

quick_style
#

unhide_when_used
#
