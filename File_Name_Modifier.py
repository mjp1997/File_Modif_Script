import os
from os import listdir
from os.path import isfile, join
import pathlib
mypath = pathlib.Path(__file__).parent.absolute()

fileExtension = input("File Extension/substring you'd like to replace: ")
newFileExtension = input("New File Extension: (press 'Enter' if none: ")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
	if fileExtension in file:
		os.rename(file, file.replace(fileExtension, newFileExtension))
