from urllib import request
import sys

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

my_url = 'http://unsdsn.org/wp-content/uploads/2013/11/FfD-logo-website-tile.jpg'
my_file = 'cartinka.jpg'

try:
    print('Start Download file from: {}'.format(my_url))
    request.urlretrieve(my_url, my_file)
except:
    print('Error!!')
    print(sys.exc_info())