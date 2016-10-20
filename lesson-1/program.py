#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "string" ////////////////

	import random

	test0 = random.randrange(1, 3)
	test1 = 'jhdjf'
	test2 = 2
	test3 = len(test1)

	ex = "test: {test[0]}".format(test = [test0, test1, test2, test3])
	ex2 = '{2},{0},{1}'.format('a', 'b', 'c')

	ex3 = '{:>30}'.format('right align')
	ex4 = '{:^30}'.format('center')

	points = 19.5
	total = 22

	ex5 = 'test: {:.2%}'.format(points/total)