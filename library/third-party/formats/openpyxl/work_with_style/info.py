# стилизация :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from openpyxl.styles import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#
Alignment(
	horizontal='general',
	vertical='bottom',
	text_rotation=0,
	wrap_text=False,
	shrink_to_fit=False,
	indent=0
)

#
Border(
	left=Side(
		border_style=None,
		color='FF000000'
	),
	right=Side(
		border_style=None,
		color='FF000000'
	),
	top=Side(
		border_style=None,
		color='FF000000'
	),
	bottom=Side(
		border_style=None,
		color='FF000000'
	),
	diagonal=Side(
		border_style=None,
		color='FF000000'
	),
	diagonal_direction=0,
	outline=Side(
		border_style=None,
		color='FF000000'
	),
	vertical=Side(
		border_style=None,
		color='FF000000'
	),
	horizontal=Side(
		border_style=None,
		color='FF000000'
	)
)

Color()
#

DEFAULT_FONT
#

Fill()
#
 
# работа с шрифтами
Font(
	name='Calibri',
	size=11,
	bold=False,
	italic=False,
	vertAlign=None,
	underline='none',
	strike=False,
	color='FF000000'
)

#
GradientFill()

#
NamedStyle()

#
NumberFormatDescriptor()

#
PatternFill(
	fill_type=None,
	start_color='FFFFFFFF',
	end_color='FF000000'
)

#
Protection(
	locked=True,
	hidden=False
)

#
Side()



alignment
#

borders
#

builtins
#

cell_style
#

colors
#
	BLACK, BLUE, DARKBLUE, DARKGREEN, DARKRED, 
	DARKYELLOW, GREEN, RED, WHITE, YELLOW

differential
#

fills
#

fonts
#

is_builtin
#

is_date_format
#

named_styles
#

numbers
#

protection
#

proxy
#

styleable
#

stylesheet
#

table
#



f2.active.sheet_properties.tabColor = "1072BA"
# подсвечивает активную вкладку