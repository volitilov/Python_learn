Font ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# предоставляет доступ к свойствам символа, таким как имя 
# шрифта, размер шрифта, полужирный шрифт и индекс. 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# получение объекта font
paragraph = Document(docx_file).paragraphs[0]
run = paragraph.runs[0]
font = run.font

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

all_caps
#

bold
#

color
#

complex_script
#

cs_bold
#

cs_italic
#

double_strike
#

emboss
#

hidden
#

highlight_color
#

imprint
#

italic
#

math
#

name
#

no_proof
#

outline
#

rtl
#

shadow
#

size
#

small_caps
#

snap_to_grid
#

spec_vanish
#

strike
#

subscript
#

superscript
#

underline
#

web_hidden
#
