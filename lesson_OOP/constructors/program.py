#	/////////////////////////////////////////////////////////
#	Here, the practice on the topic "constructors" ..........

#	Task:

#	Программа учёта закачек разных браузеров

class BrauserDownloads:
	def __init__(self, f, c, o, brausers):
		self.firefox = f
		self.chrome = c
		self.opera = o
		self.b = brausers
		self.record(f, c, o, brausers)

	def record(self, firefox, chrome, opera, b):
		b['firefox']['download'] = b['firefox']['download'] + self.firefox   
		b['chrome']['download'] = b['chrome']['download'] + self.chrome
		b['opera']['download'] = b['opera']['download'] + self.opera


