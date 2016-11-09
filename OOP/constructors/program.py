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
		self.record()

	def record(self):
		self.b['firefox']['download'] = self.b['firefox']['download'] + self.firefox
		self.b['chrome']['download'] = self.b['chrome']['download'] + self.chrome
		self.b['opera']['download'] = self.b['opera']['download'] + self.opera

