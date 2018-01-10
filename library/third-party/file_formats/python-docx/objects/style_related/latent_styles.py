LatentStyles ::::::::::::::::::::::::::::::::::::::::::::::::::

# Предоставляет доступ к стилям по умолчанию для скрытых 
# стилей в этом документе и коллекции объектов _LatentStyle, 
# которые определяют переопределения этих значений по умолчанию 
# для определенного имени скрытого стиля.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from docx import Document

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# получение объекта styles
doc = Document(docx_file)
paragraph = doc.paragraphs[0]
run_obj = paragraph.runs[0]
latent_styles = run_obj.latent_styles

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

add_latent_style(name)
#

default_priority
#

default_to_hidden
#

default_to_locked
#

default_to_quick_style
#

default_to_unhide_when_used
#

element
#

load_count
#

