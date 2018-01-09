BaseStyle :::::::::::::::::::::::::::::::::::::::::::::::::::::

# Базовый класс для различных типов объектов стиля, абзаца, 
# символа, таблицы и нумерации. Эти свойства и методы 
# наследуются всеми объектами стиля.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# получение объекта styles
doc = Document(docx_file)
paragraph = doc.paragraphs[0]
run_obj = paragraph.runs[0]
base_style = run_obj.styles.base_style

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

builtin
#

delete()
#

element
#

hidden
#

locked
#

names
#

priority
#

quick_style
#

type
#

unhide_when_used
#
