#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "encapsulation" .........

#	Task:

#	Простой пример инкапсуляции

class TestEncapsulation:
	__test = 7

	def _testFunc(self, c, x):
		return c + x

	def _sum(self, a, b):
		zzz = self._testFunc(a, b) + self._testFunc(a, b)
		zz = self._testFunc(117, 9)
		z = self.__test + a + b
		return z + zz + zzz