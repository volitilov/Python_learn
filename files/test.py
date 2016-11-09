from program import *

f = open('program.py', 'a+')

def testFunc(a, b): a + b

test = "Hellow world"
test2 = str(testFunc(5, 6))

print(f.write(test2))
print(f.close())