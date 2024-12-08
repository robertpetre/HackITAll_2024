import json

with open('investing_news.json', 'r') as f1, open('yahoo_news.json', 'r') as f2:
    json1 = json.load(f1)
    json2 = json.load(f2)
    
concatenated_json = json2

with open("concatenated.json", "w") as file:
    json.dump(concatenated_json, file, indent=4)

print("JSON has been written to 'concatenated.json'.")
