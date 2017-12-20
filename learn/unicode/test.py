from unicodedata import name, lookup

def unicode_test(value):
	value1 = name(value)
	value2 = lookup(value1)
	print('value1: {}'.format(value1))
	print('value2: {}'.format(value2))


unicode_test('A')
# value1: LATIN CAPITAL LETTER A
# value2: A

unicode_test('\u00a2')
# value1: CENT SIGN
# value2: ¢

unicode_test('\u20ac')
# value1: EURO SIGN
# value2: €

unicode_test('\u2603')
# value1: SNOWMAN
# value2: ☃


print(lookup('SNOWMAN')) # ☃
print(lookup('LATIN CAPITAL LETTER A')) # A



snowman = '\u2603'
d = snowman.encode('utf-8')
print(d) 	# b'\xe2\x98\x83'
d = d.decode('utf-8')
print(d)	# ☃

