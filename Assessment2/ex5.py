import json

file = open('ex5.json', 'r')
task = json.load(file)
file.close()  

for i in task:
    if i["name"] == "Old Fashioned" and i["type"] == "donut": 
        i["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break

file = open('ex5.json', 'w')
json.dump(task, file, indent=2)
file.close()
