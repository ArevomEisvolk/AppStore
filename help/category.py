import os
from glob import glob
import json, time
from pathlib import Path
import sys
if sys.platform == "linux":
    sys.path.append("/mnt/Datengrab/python/AreOS-Backend")
else:
     sys.path.append("/Users/are/Documents/Github/AreOS-Backend")
from untils.text_transform import merge_two_dicts
from untils.config import Config_Reader



li = []
is_app = set()
lu = []


for index, app in enumerate(glob(f"AppStore/Apps/*/appfile-{os.uname().machine}.json",recursive=True)):
            with open(app, "r") as file:
                appfile = json.load(file)
                [is_app.add("".join(app)) for app in appfile["category"]]

with open("AppStore/category-list.json", "r") as cat:
    li.append({'name': 'All', 'icon': 'apps', 'description': 'All Apps', 'id': 0,"count" : 1})
    for index, cat in enumerate(json.load(cat)):
        if cat["name"] in is_app:
            li.append(merge_two_dicts(cat,{"id":index+1, "count" : 1}))
        else:
            li.append(merge_two_dicts(cat,{"id":index+1, "count" : 0}))
            
    
ids = {}
for i in li:
    ids.update({str(i.get("id")) : i.get("name")})
        

Config_Reader().write_value("appstore","app_ids",str(ids))


with open(f"{Path(os.path.dirname(os.path.abspath(__file__))).parent.parent}/config/appstore/category.json", "w") as af:
    json.dump(li, af, indent=4)