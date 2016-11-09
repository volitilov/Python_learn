from program import Simple as s

import random
summ = 56

s = s(random, summ)
b = s 	# создаём экземпляр

print(b.r) 	# вызов random канструктора
print(b.s)	# вызов summ + 1
print(b.testFunction(5, 6))