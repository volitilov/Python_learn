#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "list" ////////////////

#	Task:

#	- Create list;

#	- Find the list item and insert in its place another;

#	- Search and replace element is dependet on the
#	  transmitted index


var = "zzzz"

testList = ["zaza", "lalka", 4223, var, " "]

def replacementElement(a):

	b = testList[a]
	testList.remove(b)
	testList.insert(a, "test")

	return testList
