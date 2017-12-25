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



with open(file_name, 'w') as file:
	json.dump(players, file)
	# преобразование в json и запись в файл 


# load by json ::::::::::::::::::::::
with open(file_name) as file:
	json_data = json.load(file)
	# преобразование json в python формат

	for user in json_data:
		print(user["name"])