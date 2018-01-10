from openpyxl import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

f = Workbook()
sheet = f.active
sheet.title = 'Work_list'

for x in range(1, 10):
	sheet.append([x])


data = chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
chart = chart.BarChart()
chart.add_data(data)
sheet.add_chart(chart, 'C2')

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

f.save('file.xlsx')