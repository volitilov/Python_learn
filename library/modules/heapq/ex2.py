import heapq

# ::::::::::::::::::::::::::::::::::::::::::::

class PrioretyQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]



class Item:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)



q = PrioretyQueue()
q.push(Item('Bob'), 5)
q.push(Item('Sam'), 3)
q.push(Item('Din'), 4)
q.push(Item('Dic'), 1)
q.push(Item('Alex'), 2)

print(q.pop()) # Item('Bob')
print(q.pop()) # Item('Din')
print(q.pop()) # Item('Sam')
print(q.pop()) # Item('Alex')
print(q.pop()) # Item('Dic')
