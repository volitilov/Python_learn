python-docx ::::::::::::::::::::::::::::::::::::::::::::::::::::

# python-docx - это библиотека Python для создания и обновления
# файлов Microsoft Word (.docx).

# документация на английском:
# https://python-docx.readthedocs.io/en/latest/

# установка:
pip install python-docx

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

doc = Document('demo.docx')

paragraph = doc.paragraphs[0]

run_obj = paragraph.runs[0]

font = run_obj.font

style = run_obj.style

color = run_obj.style.color

color_format = color.ColorFormat

tab_stop = paragraph.tabstops[0]



