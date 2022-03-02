import json

with open("/Users/are/Documents/Github/AreOS-Backend/config/appfile.json", "r") as file:
	appfile = json.load(file)
	for i in appfile.get("list"):
		if i.get("id") == 3:
			print(i.get("container").get("image"))