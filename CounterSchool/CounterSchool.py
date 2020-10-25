import os
import concurrent.futures
import threading
import time
import string


available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


thread_local = threading.local()

test = int(input("1, auto. 2, Manual:"))

def auto():
    if test == 1:
        DriveNum = 1
        Dirname = '/Program Files/'
        appname = "7z"

    if test == 2:
        DriveNum = int(input("Drive name in alphabetical order(eg; a=1, b=2, f=3):"))
        Dirname = '/' + str(input("First folder:")) + '/'
        appname = str(input("App Name:"))
        return Dirname, DriveNum, appname
    return Dirname, DriveNum, appname

DriveNum = auto()[1]
Dirname = auto()[0]
appname = auto()[2]

fileextent = '.exe'
DriveNumFin = int(DriveNum) - 1

basepath = available_drives[DriveNumFin] + Dirname

filename = appname + fileextent

with os.scandir(basepath) as entries:
    for entry in entries:
            if entry.is_dir():
               subpath = basepath + entry.name
               with os.scandir(subpath) as entries:
                for entry in entries:
                            if entry.is_file():
                                if entry.name == filename:
                                        print("Located")
                                        print(entry.path)
                            if entry.is_dir():
                                subpath = subpath + "/" + entry.name

                                with os.scandir(subpath) as entries:
                                                    for entry in entries:
                                                        if entry.is_file():
                                                            if entry.name == filename:
                                                                    print("Located")
                                                                    print(entry.path)
            else:
                print("Not found")