import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::

def calcPod():
	a = 1
	for i in range(1, 100000):
		a *= i
	return a

start = time.time()
res = calcPod()
end = time.time()

print(len(str(res)))
print(end - start)