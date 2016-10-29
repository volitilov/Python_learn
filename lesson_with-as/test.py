from program import *

with open('program.py', 'a', encoding='utf-8') as g:
    d = str(input())
    print(d, file=g)