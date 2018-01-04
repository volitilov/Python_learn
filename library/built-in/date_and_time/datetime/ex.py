import datetime as dt

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

n_e = dt.datetime(2017, 12, 31, 0, 0, 0)

while dt.datetime.now() < n_e:
	time.sleep(1)

print('Happy new year !!!')
