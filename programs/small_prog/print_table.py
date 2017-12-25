#!/usr/bin/python3

# print_table.py 
# принимает список списков строк и отображает его в виде 
# аккуратной таблицы с выравниванием текста по правому краю 
# в каждом столбце.

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# import pyperclip

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

tableData = [
	['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose']
]

def printTable(tableData):
	max_string = ''

	for x in tableData:
		for y in x:
			if len(y) > len(max_string): 
				max_string = y

		# TODO: сделать столбцы
		# TODO: выровнить текст по правому краю


printTable(tableData)