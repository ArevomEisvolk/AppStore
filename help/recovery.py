import os
from glob import glob
import json, time
from pathlib import Path
import sys
sys.path.append("/mnt/Datengrab/python/AreOS-Backend")
from untils.config import Config_Reader

def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    print(z)
    return z

def replace_dict_id(x,  ids):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    x["id"] = ids
    return x

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
            
    
a = Config_Reader("config/config.ini")

a.write_category(str(lu))

with open(f"{Path(os.path.dirname(os.path.abspath(__file__))).parent.parent}/config/category.json", "w") as af:
    json.dump(li, af, indent=4)