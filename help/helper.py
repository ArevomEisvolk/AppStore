import os
from glob import glob
import json, time
from pathlib import Path
import sys
sys.path.append("/mnt/Datengrab/python/AreOS-Backend")
from datastructs.docker_app import App

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

def get_dict_value(dic, *args):
    value = dict()
    for i in args:
        value.update({i : dic.get(i)})
    return value
        
def uebersetzer(name):
    des = {"overview" : "description"}

def container_extractor(dic, container_des):
    for i in dic.get(container_des):
       dic.get(container_des).get(i)
        
def log(inou):
    with open("./log.json", "w") as f:
        f.write(inou)
    
li =[]

for index, app in enumerate(glob("AppStore/Apps/*/appfile.json",recursive=True)):
    with open(app, "r") as file:
        appfile = json.load(file)
        dic = get_dict_value(appfile,"title","name","icon","thumbnail","screenshots","container","tagline","category","tips","developer","adaptor","constraints",)

        a = App(
            title           = dic["title"],
            description     = dic["tagline"],
            tagline         = dic["tagline"],
            tags            = "null",
            icon            = dic["icon"],
            screenshot_link = dic["screenshots"],
            category        = dic["category"],
            category_font   = "cloud-outline",
            port_map        = dic["container"]["ports"][0]["host"] if len(dic["container"]["ports"]) != 0 else "null",
            image_version   = dic["container"]["image"].split(":")[1],
            tip             = "[]" if dic["tips"] == {} else json.dumps(dic["tips"]["before_install"]),
            envs            = dic["container"]["envs"],
            ports           = dic["container"]["ports"],
            volumes         = dic["container"]["volumes"],
            devices         = dic["container"]["devices"],
            network_model   = dic["container"]["network_model"],
            image           = dic["container"]["image"].split(":")[0],
            index           = "/",
            created_at      = time.time(),
            updated_at      = time.time(),
            state           = "",
            author          = dic["adaptor"]["name"],
            min_memory      = dic["container"]["constraints"]["min_memory"],
            min_disk        = dic["container"]["constraints"]["min_storage"],
            thumbnail       = dic["thumbnail"],
            healthy         = "",
            plugins         = "null",
            origin          = "offical",
            type            = 0,
            developer       = dic["developer"]["name"],
            host_name       = "",
            privileged      = dic["container"]["privileged"],
            cap_add         = dic["container"]["cap_add"],
            cmd             = "null"
        )

        li.append(replace_dict_id(a.__repr__(),index+1))

    

with open(f"{Path(os.path.dirname(os.path.abspath(__file__))).parent.parent}/config/appstore.json", "w") as af:
    json.dump({"list" : li, "community" : [], "recommend" : []}, af, indent=4)
        