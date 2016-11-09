#   //////////////////////////////////////////////////////////
#   program test learn .......................................

#	
a = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

#	example 1
# for i in range(len(a)):
# 	for j in range(len(a[i])):
# 		print(a[i][j], end=' ')
# 	print()

#	example 2
# s = 0
# for x in a:
# 	for t in x:
# 		s += t 
# 	print(s)

#	example 3
# n = 5
# m = 5
# a = [0] * n
# for i in range(n):
#     a[i] = [0] * m
# print(a)

#	example 4
n = 3
m = 5
a = [[' '] * m for i in range(n)]
print(a)