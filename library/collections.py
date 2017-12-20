# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# collections

from collections import Counter
mas = [1, 2, 3, 4, 4, 4]
mas2 = mas
Counter(mas) # Counter({4: 3, 1: 1, 2: 1, 3: 1})
a = Counter(mas)
b = Counter(mas2)
a + b # Counter({4: 6, 1: 2, 2: 2, 3: 2})
a - b # Counter({})


from collections import OrderDict
# запоминает порядок, в котором добавлялись ключи, и 
# возвращает их в том же порядке с помощью итератора
ex = OrderDict([('a',1), ('b',2), ('c',3)])
for i in ex: i # a  b  c
