import os
from glob import glob
import json

for i in glob("AppStore/Apps/*/appfile.json",recursive=True):
    appfile = json.load(open(i))
    for var in ["title", "tagline", ""]:
        appfile[var]