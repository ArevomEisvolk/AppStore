
import os
from glob import glob
import json, time
from pathlib import Path
import sys
if sys.platform == "linux":
    sys.path.append("/mnt/Datengrab/python/AreOS-Backend")
else:
     sys.path.append("/Users/are/Documents/Github/AreOS-Backend")
from untils.config import Config_Reader
from untils.text_transform import merge_two_dicts



li = []
is_app = set()
lu = []


for index, app in enumerate(glob("AppStore/Apps/*/appfile.json",recursive=True)):
            with open(app, "r") as file:
                appfile = json.load(file)
                is_app.add("".join(appfile["category"]))

with open("AppStore/category-list.json", "r") as cat:
    li.append({'name': 'All', 'icon': 'apps', 'description': 'All Apps', 'id': 0,"count" : 1})
    for index, cat in enumerate(json.load(cat)):
        if cat["name"] in is_app:
            li.append(merge_two_dicts(cat,{"id":index+1, "count" : 1}))

            lu.append({"category": cat["name"] , "id": index+1})
            



ids = {}
for i in li:
    ids.update({str(i.get("id")) : i.get("name")})
        

Config_Reader().write_value("appstore","app_ids",str(ids))


