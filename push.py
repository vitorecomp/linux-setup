#!/usr/bin/env python3

import os 
import shutil 
from os.path import expanduser

#create the resource folder
resource_folder = './resource'
if not os.path.exists(resource_folder):
    os.mkdir(resource_folder)
	
#copy the i3 config file
home = expanduser("~")
source = home + '/.config/i3'
print(source)
destination = resource_folder + '/config'

shutil.copytree(source, destination)
