from openpyxl import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

f = Workbook()
sheet = f.active
sheet.title = 'Work_list'

for x in range(1, 10):
	for y in range(1, 10):
		cell = sheet.cell(row=y, column=x)
		cell.value = x + y


sheet['A1'].font = styles.Font(size=15, bold=True)

f.save('file.xlsx')