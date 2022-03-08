import os
from glob import glob
import json
from pathlib import Path

def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

li =[]

for index, app in enumerate(glob("AppStore/Apps/*/appfile.json",recursive=True)):
    with open(app, "r") as file:
        appfile = json.load(file)
        li.append(merge_two_dicts({"id" : index+1},appfile))

    
print()
with open(f"{Path(os.path.dirname(os.path.abspath(__file__))).parent.parent}/config/appstore.json", "w") as af:
    json.dump({"list" : li, "community" : [], "recommend" : []}, af, indent=4)
        