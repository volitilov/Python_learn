import openpyxl

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

f = openpyxl.load_workbook('example.xlsx')
# print(f.get_sheet_names())
sheet = f.get_sheet_by_name('Лист1')
# print(f.get_sheet_by_name('Лист1').title)
# print(f.get_active_sheet())
# print(f.active.title)

c = sheet['B1']
print('Ячейка {}: {}, кол-во: {}'.format(c.coordinate, 
	c.value, sheet['C1'].value))

print(sheet.cell(row=1, column=2))

