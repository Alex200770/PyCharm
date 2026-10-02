import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    with open(json_path, encoding='utf-8') as json_file:
        users_data: dict[str, str] = json.load(json_file)
        # print(users_data)

    with open(csv_path, 'w', encoding='utf-8') as csv_file:
        fieldnames = list(users_data[0].keys())
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users_data)

# with open('people.json', 'w', encoding='utf-8') as text:

json_to_csv('people.json', 'people.csv')

