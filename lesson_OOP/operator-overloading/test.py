from program import Overloading as O, Redefinition as R

c =  0
o = O(5, 6, c)
r = R(10, 5, c)

print(o.c)
print(r.c)