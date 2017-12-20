import json

# ::::::::::::::::::::::::::::::::::::::::::::::::

file_name = 'user_settings.json'

player1 = {
	"name": "Barak Obama",
	"score": 3333,
	"awards": ['OR', 'NW', 'NY']
}

player2 = {
	"name": "Donald Tramp",
	"score": 44444,
	"awards": ['WT', 'DT', 'CA', 'TX']
}

players = [player1, player2]

# save by json ::::::::::::::::::::::
file = open(file_name, 'w')
json.dump(players, file)
file.close()

# load by json ::::::::::::::::::::::
file = open(file_name)
json_data = json.load(file)

for user in json_data:
	print(user["name"])
file.close()