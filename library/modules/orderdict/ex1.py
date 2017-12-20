from collections import OrderedDict
import json

# ::::::::::::::::::::::::::::::::::::::::::::::::::

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3

for key in d:
	print(key, d[key])
# 'a 1', 'b 2', 'c 3'

print(d)
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print(json.dumps(d))
# {"a": 1, "b": 2, "c": 3}
