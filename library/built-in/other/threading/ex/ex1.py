from threading import Thread
import time

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def takeANap():
	time.sleep(2)
	print('th: thObj')

thObj = th.Thread(target=takeANap)
thObj2 = th.Thread(target=print, args=['th','thObj2'], kwargs={'sep': ': '})
thObj3 = th.Thread(target=print, args=['th: thObj3', str(1)])
thObj4 = th.Thread(target=print('th: thObj4'))

th_list = [thObj, thObj2, thObj3]

for i in th_list:
	i.daemon = True
	i.start()

