from program import BrauserDownloads

brausers = {
	'firefox': {
		'download': 0
	},
	'chrome': {
		'download': 0
	},
	'opera': {
		'download': 0
	}
}

BrauserDownloads(45, 76, 34, brausers) # day 1
print(brausers)
BrauserDownloads(5, 6, 4, brausers) # day 2
print(brausers)