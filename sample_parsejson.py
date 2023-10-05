import json
import yaml

#example of json
x ='{"name": "Sean","age": "22", "city": "Antipolo City"}'

#parse json
y = json.loads(x)
print("The output of json file is ", y)
print("Age: ", y["age"])
print("Name: ",y["name"])
print("City:", y["city"])