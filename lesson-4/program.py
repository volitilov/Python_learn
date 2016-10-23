#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "tuple" ////

#	Task:

#	- создать кортеж и сделать срез по переданным 
#	  параметрам

var = (1, 2, 3, 4, 5)

def slices(a, b):

	testTuple = (1, 2, 3, "sds", 247, var)

	slices = testTuple[a:b]

	return slices