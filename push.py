#!/usr/bin/env python3

import os 
import shutil 
from os.path import expanduser

#create the resource folder
resource_folder = './resource'
if not os.path.exists(resource_folder):
    os.mkdir(resource_folder)
	
home = expanduser("~")
#copy the i3 config file
source = home + '/.config/i3'
destination = resource_folder + '/config'

shutil.copytree(source, destination)


#copy bash file
source = home + '/.zshrc'
os.mkdir(resource_folder+ '/bash')
destination = resource_folder + '/bash/.zshrc'

shutil.copyfile(source, destination)
