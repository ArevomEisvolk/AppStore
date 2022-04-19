from glob import glob
import os



print(os.uname().machine)
#for index, app in enumerate(glob("AppStore/Apps/*/appfile.json",recursive=True)):
	#os.rename(app,app.replace(".json", "-x86_64.json"))