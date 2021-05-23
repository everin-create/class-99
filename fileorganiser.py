import os
import shutil

path=input("Provide the path of the directory to be sorted. ")

# This helps get the files in the path

list_of_files=os.listdir(path)
print(list_of_files)

#This funtion reads the name and extensions of the file do we can sort by extension

for file in list_of_files:
    name,ext=os.path.splitext(file)

    ext=ext[1:]

#This is to make sure there are folders to put the respective files in

    if ext=='':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
