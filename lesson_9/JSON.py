import json

price_dict: dict[str, int] = {
    'Bread': 100,
    'Butter': 200,
    'Apples': 300
}


with open('prices.json', 'w') as prices_file:
    json.dump(price_dict, prices_file, indent=4)

with open('prices.json', 'r') as prices_json:
    prices = json.load(prices_json)

print(prices)
