#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "indexes and slices" ////

#	Task:

#	- сгенерировать список и сделать срез взависимости от 
#	- передоваемых параметров

var = "zazazazazaza"

def slices(a, b):

	testList = [c * 1 for c in var if c != 'a']

	slices = testList[a:b]

	return slices