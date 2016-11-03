from program import SuperClass, SelfTest

x = 0
y = 0
ex3 = 'oli'

s2 = SelfTest(ex3, x, y)

print(s2.sum(9, 6))		# 15
print(s2.c1)			# {'oli': 0}
print(s2.c2)			# {'oli': 19}