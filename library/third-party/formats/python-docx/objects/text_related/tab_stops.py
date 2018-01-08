TabStops ::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Последовательность объектов TabStop, обеспечивающая доступ к 
# табуляторам стоп стиля абзаца. Поддерживает итерацию, 
# индексированный доступ, del и len().

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# получение объекта font
paragraph = Document(docx_file).paragraphs[0]
tab_stops = paragraph.tabstops

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

add_tab_stop(position, 
	alignment=WD_TAB_ALIGNMENT.LEFT, 
	leader=WD_TAB_LEADER.SPACES)
#

clear_all()
#
