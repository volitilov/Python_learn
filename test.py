# i = 5

# while i < 15:
# 	print(i)
# 	i += 1
	

# ////////////////////////////////////

# test1 = 34
# test2 = 57

# if test1 < 50 and test2 > 50:
# 	print("Hellow")

# ////////////////////////////////////

# name = bool("Slava")

# if name == True:
# 	print("Hellow")
# else:
# 	print("Bad")

# //////////////////////////////////////

# import random 	#импортируем модуль

# test = random.randrange(1, 10)
# print(test)

# ////////////////////////////////////////

# для длиного текста применяются ('''example''')
# test = '''jwejwegr 2364527 sdjfhgsjdf
# 		5142315341341 764524726425273
# 		jsdfhgsjfgsjsfdhsdfhsdfgjshsj
# 	   '''

# # методы работы со строками
# print(len(test)) 			# длина строки
# print(test[27])				# обращение по индексу
# print(test[3:8])			# делаем срез по индексу от, до
# print(test[1:27:2])			# делаем срез с шагом
# print(test.isdigit())		# состоит ли строка из цифр
# print(test.isalpha())		# состоит ли строка из букв
# print(test.isalnum())		# состоит ли строка из цифр и букв
# print(test.islower())		# сотсоит ли строка из символов в нижнем регистре
# print(test.isupper())		# состоит ли строка из символов в верхнем регистре
# print(test.upper())			# преобразование строки к верхнему регистру
# print(test.lower())			# преобразование строки к нижнему регистру
# print(test.capitalize())	# переводит первый символ строки в верхний регистр, а все остальные в нижний

# ////////////////////////////////////////////

# форматирование строк
import random

test0 = random.randrange(1, 3)
test1 = 'jhdjf'
test2 = 2
test3 = len(test1)

print("test: {test[0]}".format(test = [test0, test1, test2, test3]))
print('{2},{0},{1}'.format('a', 'b', 'c'))