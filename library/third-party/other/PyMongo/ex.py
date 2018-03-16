#!/usr/bin/python3

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from atexit import register
from pymongo import MongoClient

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def _main():
	client = MongoClient('localhost', 27017)
	# client = MongoClient('mongodb://localhost:27017/')


@register
def _atexit(): pass



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
