from program import Security

ex2 = Security('oli', '29')
print(ex2.test())
ex3 = Security('vik', '16')
print(ex3.test())
ex3 = ex2
print(ex3.test())