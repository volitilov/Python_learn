#!/usr/bin/python3

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from atexit import register
import sqlalchemy

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def _main():
	print(sqlalchemy.__version__)

@register
def _atexit(): pass



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
