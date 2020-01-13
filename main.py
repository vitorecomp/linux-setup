#!/usr/bin/env python3

import os 
import shutil 
from os.path import expanduser

#copy the i3 config file
resource_folder = './resource'	
source = resource_folder + '/config'
home = expanduser("~")
destination = home + '/.config/i3'

shutil.copytree(source, destination)

#creating worksapce directory
workspace = home + '/workspace'
if not os.path.exists(workspace):
    os.mkdir(workspace)

folders = ['cloud', 
'master',
'opensource',
'personal',
'presentations',
'work'
]

for i in folders:
	folder = workspace + '/' + folders[i]
	if not os.path.exists(folder):
		os.mkdir(folder)

#clonig respositories

#creting tools directory
tools = home + '/tools'
if not os.path.exists(tools):
    os.mkdir(tools)


