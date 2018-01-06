#!VENV/bin/python3

# run_fruits.py
# - считает остаток кг.
# - считает выручку с продажи каждой категории товара
# - считает выручку с продажи всех товаров
# - заносит данные продаж в таблицу

# Использование: 
	# python run_fruits.py
	# поситать данные


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from openpyxl import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

file = load_workbook('fruits.xlsx')
sheet = file.active

for row in list(sheet.rows)[1:]:
	# считаю остаток кг вида товаров и присваивает значение ячейки
	row[4].value = int(row[2].value) - int(row[3].value)
	# считаю выручку вида товаров и присваивает значение ячейки
	row[6].value = float(row[1].value) * int(row[3].value) 


file.save('fruits.xlsx')