import json
from pprint import pprint
import requests
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
respons = requests.get(url)
data = respons.json()
name = ['Hulk', 'Captain America', 'Thanos']#, 'A-Bomb', 'Agent Zero', 'Agent Bob']
heros = []
for ii in name:
    for item in data:
        if item['name'] == ii:
            heros.append({'name': ii, 'intelligence': item['powerstats']['intelligence']})
super_heros = sorted(heros, key=lambda name: name['intelligence'])
super_hero = super_heros[-1] # ничего умного не придумал как только от сортровать и взять с большим iQ последний в списке
# pprint(heros)
# print('**************')
pprint(super_heros)
print('**************')
print(f"Самый умный {super_hero['name']} с интелектом: {super_hero['intelligence']}")