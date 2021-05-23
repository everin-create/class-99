import os
import shutil
source=input("Enter source folder name ")
destination=input("Enter destination folder name ")

#This is to look inside the folders

source=source+'/'
destination=destination+'/'

list_of_files= os.listdir(source)

#The copy function does both copy and paste.

for file in list_of_files:
    shutil.copy((source+file),destination)
