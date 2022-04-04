import os
from glob import glob
import json, time
from pathlib import Path
import sys
if sys.platform == "linux":
    sys.path.append("/mnt/Datengrab/python/AreOS-Backend")
else:
     sys.path.append("/Users/are/Documents/Github/AreOS-Backend")
from datastructs.docker_app import App




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
            title           = dic.get("title"),
            description     = dic.get("tagline"),
            tagline         = dic.get("tagline"),
            icon            = dic.get("icon"),
            web_ui          = dic.get("container").get("web_ui"),
            screenshot_link = dic.get("screenshots"),
            category        = dic.get("category"),
            category_font   = "cloud-outline",
            port_map        = dic.get("container").get("ports")[0].get("host") if len(dic.get("container").get("ports")) != 0 else "null",
            image_version   = dic.get("container").get("image").split(":")[1],
            tip             = None if dic.get("tips") == {} else json.dumps(dic.get("tips").get("before_install")),
            envs            = dic.get("container").get("envs"),
            ports           = dic.get("container").get("ports"),
            volumes         = dic.get("container").get("volumes"),
            devices         = dic.get("container").get("devices"),
            network_model   = dic.get("container").get("network_model"),
            image           = dic.get("container").get("image").split(":")[0],
            index           = dic.get("container").get("web_ui").get("path"),
            min_memory      = dic.get("container").get("constraints").get("min_memory"),
            min_disk        = dic.get("container").get("constraints").get("min_storage"),
            thumbnail       = dic.get("thumbnail"),
            developer       = dic.get("developer").get("name"),
            privileged      = dic.get("container").get("privileged"),
            cap_add         = dic.get("container").get("cap_add"),
        )

        li.append(replace_dict_id(a.__repr__(),index+1))

    

with open(f"{Path(os.path.dirname(os.path.abspath(__file__))).parent.parent}/config/appstore/appstore.json", "w") as af:
    json.dump({"list" : li, "community" : [], "recommend" : []}, af, indent=4)
        