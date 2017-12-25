from collections import defaultdict

# :::::::::::::::::::::::::::::::::::::::::::::::::::::

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(1)

print(d)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [1]})

d = defaultdict(set)

d['a'].add(1)
d['a'].add(2)
d['b'].add(1)

print(d)
# defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {1}})

