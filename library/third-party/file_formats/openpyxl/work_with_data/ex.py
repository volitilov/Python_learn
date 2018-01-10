import openpyxl

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

f = openpyxl.load_workbook('fruits.xlsx')
f2 = openpyxl.Workbook()

# sheet = f.get_sheet_by_name('Лист1')
sheet = f.get_active_sheet()



if __name__ == '__main__':
	# print(f.get_sheet_names())
	# print(f.get_sheet_by_name('Лист1').title)
	# print(f.get_active_sheet())
	# print(f.active.title)

	# c = sheet['B1']
	# print('Ячейка {}: {}, кол-во: {}'.format(c.coordinate, 
	# 	c.value, sheet['C1'].value))

	# print(sheet.cell(row=1, column=2))

	# print(tuple(sheet['A1':'C3']))

	# for item, row in enumerate(sheet['A1':'C3']):
	# 	print('\nСтока: {}'.format(item+1))
	# 	for cell in row:
	# 		print('ячейка: {} - {}'.format(cell.coordinate, cell.value))
	
	print(list(sheet.columns)[1])
