from importlib.resources import path
import os
import shutil

def calculate_photos():
    count = 0
    for pathcwd,dirname,filename in os.walk(os.getcwd()):
        for filenames in filename:
            extention = os.path.splitext(os.path.join('/',filenames))[-1]
            if(extention == ".jpg" or extention == ".png"):
                count += 1
    print(count)

def copy_photos():
    for pathcwd,dirname,filename in os.walk(os.getcwd()):
        for filenames in filename:
            extention = os.path.splitext(os.path.join('/',filenames))[-1]
            filename = os.path.splitext(os.path.join('/',filenames))[0]
            if(extention == ".jpg" or extention == ".png"):
                filepath = os.path.join(pathcwd ,filenames)
                if(filenames[:3] == "img" or filenames[:3] == "IMG"):
                    year = filenames[4:8]
                    month = filenames[8:10]
                    if(int(year) > 2010 and int(month) <= 12):
                        if(os.path.isdir(os.path.join(year , month)) == False):
                            os.makedirs(os.path.join(year , month))

                        final = os.path.join(year , month)
                        shutil.move(filepath , final)


copy_photos()
input = input()