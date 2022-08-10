# Testing storing data a certain way for app:
import json

with open("expense_data.json", "r") as file:
    jsonData = json.load(file)
print("Datatype of variable: ", type(jsonData))
for i in jsonData.keys():
    print(i)
    
    #print(jsonData[i]["cost"], jsonData[i]["cost_per"])

print(jsonData["paper towels"]["cost_per"])
print(jsonData["needles #5"]["cost_per"])
