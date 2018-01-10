import csv

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

with open('ex_file.csv') as file:
	csv_file = csv.reader(file)

# 	# print(csv_file.line_num) # 0
# 	# print(next(csv_file))
# 	# print(next(csv_file))
# 	# print(csv_file.line_num) # 2

	for line in list(csv_file):
		print(line)

# with open('ex_file2.tsv', 'w', newline='') as file:
# 	csv_file = csv.writer(file, delimiter='\t')
# 	csv_file.writerow(['1.04.2015', 'Вишня', '48'])
# 	csv_file.writerow(['2.04.2015', 'Яблоки', '40'])
# 	csv_file.writerow(['3.04.2015', 'Груши', '48'])
# так как я использую табуляцию в качестве разделителя 
# теперь файл имеет расширение .tsv


