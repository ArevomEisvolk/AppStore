import os
from glob import glob
import json
from pathlib import Path

def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

def get_dict_value(dic, *args):
    value = dict()
    for i in args:
        value.update({i : dic.get(i)})
    return value
        
        
        
    
    
li =[]

for index, app in enumerate(glob("AppStore/Apps/*/appfile.json",recursive=True)):
    with open(app, "r") as file:
        appfile = json.load(file)
        dic = get_dict_value(appfile,"title","name","icon","screenshots","container")
        print(dic)   
        #li.append(merge_two_dicts({"id" : index+1},appfile))

    

with open(f"{Path(os.path.dirname(os.path.abspath(__file__))).parent.parent}/config/appstore.json", "w") as af:
    json.dump({"list" : li, "community" : [], "recommend" : []}, af, indent=4)
        