#!/usr/bin/python3

from nntplib import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	with NNTP('news.gmane.org') as n:
		resp, count, first, last, name = n.group('gmane.comp.python.committers')
		print('Group', name, 'has', count, 'articles, range', first, 'to', last)
		
		resp, overviews = n.over((last - 9, last))
		
		for id, over in overviews:
			print(id, decode_header(over['subject']))

		resp, number, message_id = n.stat(first)
		print(message_id)

		respo, info = n.article(message_id)
		print(len(info.lines))

		for line in info:
			print(line)

