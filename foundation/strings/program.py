#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "string" ////////////////

#	Task:

#	Зделать программу которая будет подставлять в строку 
#	значение выбранного элемента списка


name = "zaza"

def workLines():

	ex = "hellow {testList[0]}".format(testList = [name, "jhrjh", 987])

	return ex.capitalize()