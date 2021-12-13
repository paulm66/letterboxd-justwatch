import json

data = {}
with open('movie_providers.json') as f:
    data = dict(json.load(f).items())

print('technical_name, short_name, clear_name, monetization_types')
for item in data['providers']:
	print(item.get('technical_name') + ", " + item.get('short_name') + ", " + item.get('clear_name') + ", " + str(item.get('monetization_types')))