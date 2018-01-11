# Работа с данными :::::::::::::::::::::::::::::::::::::::::::::::::::::

import openpyxl

# чтение данных ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

f = openpyxl.load_workbook('example.xlsx')
# принимает файл в качестве аргумента и возвращает значение типа 
# Workbook. Объект Workbook представляет файл Excel подобно тому как 
# объект File предоставляет открытый текстовый файл.

# f.get_sheet_names()
f.sheetnames
# получение списка листов, входящих в состав рабочей книги

f.copy_worksheet(source)
# копирует рабочий лист

sheet = f.get_sheet_by_name('Лист1')
# получаем объект листа Worksheet, передав строку с именем листа

f.active
# получаем активный лист.
	title
	# получение имени

	values
	# получение объекта генератора значений

	cell(row=1, column=2, value=10)
	# получение или обращение к ячейке

	iter_cols(min_row=1, max_col=3, max_row=2)
	# создаёт генератор из колонок, отфильтрованых по заданным 
	# параметрам 

	iter_rows(min_row=1, max_col=3, max_row=2)
	# создаёт генератор из рядов, отфильтрованных по заданным 
	# параметрам

	columns
	# получение объекта генератора состоящего из кортежей колонок

	rows
	# получение объекта генератора состоящего из кортежей строк

	merge_cells('A2:D2')
	merge_cells(start_row=2,start_column=1,end_row=2,end_column=4)
	# объединение ячеек

	unmerge_cells('A2:D2')
	unmerge_cells(start_row=2,start_column=1,end_row=2,end_column=4)
	# разъеденение ячеек

	column_dimensions['A']
	# задаёт ширину столбцов
		group('A','D', hidden=True)
		# скрыть группу столбцов
		width
		# устанавливает ширину столбца

	active_cell
	#

	add_chart
	#

	add_data_validation
	#

	add_image
	#

	add_print_title
	#

	add_table
	#

	append
	#

	auto_filter
	#

	calculate_dimension
	#

	conditional_formatting
	#

	data_validations
	#

	dimensions
	#

	encoding
	#

	evenFooter
	#

	evenHeader
	#

	firstFooter
	#

	firstHeader
	#

	formula_attributes
	#

	freeze_panes = cell
	# блакирует позицию ячейки. Чтобы отменить блакирование
	# всех закреплённых областей, установите значении 'None' 

	get_cell_collection
	#

	get_named_range
	#

	get_squared_range
	#

	legacy_drawing
	#

	max_column
	# получение номера последней солонки

	max_row
	# получение номера последнего ряда

	merged_cell_ranges
	#

	merged_cells
	#

	mime_type
	#

	min_column
	#

	min_row
	#

	oddFooter
	#

	oddHeader
	#

	orientation
	#

	page_breaks
	#

	page_margins
	#

	page_setup
	#

	paper_size
	#

	parent
	#

	path
	#

	point_pos
	#

	print_area
	#

	print_options
	#

	print_title_cols
	#

	print_title_rows
	#

	print_titles
	#

	protection
	#

	row_dimensions[num]
	# управляет высотой строк
		height
		# устанавливает высоту строки

	selected_cell
	#

	set_printer_settings
	#

	sheet_format
	#

	sheet_properties
	#

	sheet_state
	#

	sheet_view
	#

	show_gridlines
	#

	show_summary_below
	#

	show_summary_right
	#

	sort_state
	#

	vba_code
	#

	views
	#


sheet['A1']
#
	value
	# содержит значение хранящееся в ячейке 
	row
	# содержит информацию о расположении данной ячейки в ряду
	column
	# содержит информацию о расположении данной ячейки в колонке
	coordinate
	# содержит координаты ячеки 
	write(index, value)
	# запись в ячейку


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
from openpyxl.utils import get_column_letter, column_index_from_string

column_index_from_string('AA')
# преобразование буквенного обозначение столбца в цифровое

get_column_letter(5)
# преобразование цифрового обозначение столбца в буквенное



# изменение данных ::::::::::::::::::::::::::::::::::::::::::::::::::::::

f2 = openpyxl.Workbook(guess_types=False, data_only=False, keep_vba=False)
# создаёт новый пустой объект Workbook
	guess_types
	# будет включать или отключать(по умолчанию) преобразование типов при 
	# чтении ячеек.
	data_only
	# если False, то в ячейку будет записан результат вычеслнгие формулы
	# если True, то в ячейку будет записана сама формула
	keep_vba
	#


f2.active.title = 'Experements'
# переименование активного рабочего листа

# f2.create_sheet(index=1, title=name)
f2.create_sheet(name, index)
# возвращает новый объект Worksheet, с именем name, который по умолчанию
# становится последним листом книги. При желании можно задать с помощью
# именованых аргументов index и title, не только имя но и индекс 
# создаваемого листа.

f2.remove_sheet(f2.get_sheet_by_name(name))
# принемает в качестве аргумента не строку с именем листа, а объект
# Worksheet. 

f2.active['A1'] = text
# запись в ячейку

f2.active.append(list)
# можно вставить сразу список значений в строку по очереди
  
f2.save(filename)
# сохранение изменений, если filename отлчается от объекта Workbook
# то он создаст новый файл с заданным именем, если имя будет 
# отсутствовать, то выкенет исключение.

f2.template
# Если True, то будет сохранять как шаблон