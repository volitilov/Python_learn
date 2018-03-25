#!/usr/bin/python3

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class ReverseString:
	def __init__(self, s):
		self.__s = s

	def __iter__(self):
		self.__i = 0
		return self

	def __next__(self):
		if self.__i > len(self.__s) - 1:
			raise StopIteration
		else:
			a = self.__s[-self.__i - 1]
			self.__i = self.__i + 1
			return a


def _main():
	s = ReverseString('Python')
	for a in s: print(a, end='')



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()


