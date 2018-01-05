from openpyxl import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

f = Workbook()
sheet = f.active
sheet.title = 'Work_list'

for x in range(1, 10):
	for y in range(1, 10):
		cell = sheet.cell(row=y, column=x)
		cell.value = x + y


sheet['A3'] = '=SUM(A1:A2)'
sheet['A3'].font = styles.Font(color=styles.colors.RED)


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

f.save('file.xlsx')