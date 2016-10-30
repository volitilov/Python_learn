# import program as p

# test = p.testModul(5, 6)
# print(test)

# from program import testModul as tm
# print(tm(8, 9))

from program import (testModul as tm, testModul2 as tm2,
					 testModul3 as tm3, testModul4 as tm4)

print(round(tm4(25, 4)))