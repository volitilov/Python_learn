from program import *

zaza = {}
zaza2 = zaza["sjdfs"] = 4

def testDef(a, b):
	return a + b,

testDict = {
	'key1': 12,
	'key2': "sjdh",
	'key3': zaza,
	'key4': testDef(5, 6),
	'key5': zaza2 
}

a = addKeyValue('lalka', '3zaza', testDict);

print('Lalka is Bzaza:', a['Lalka'] == 'Bzaza');

