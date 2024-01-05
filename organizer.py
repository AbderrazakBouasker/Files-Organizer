#!/usr/bin/env python3
import os
os.chdir('C:\\Users\\abder\\Downloads')
directorys=('Images','Videos','Documents','Compressed','Programs','Others')
Images=['.jpg','.png','.gif','.jpeg','.ico','.svg']
Videos=['.mp4','.mkv','.avi','.flv','.wmv','.mov']
Documents=['.pdf','.docx','.doc','.txt','.xlsx','.xls','.pptx','.ppt','.csv']
Compressed=['.zip','.rar','.7z','.tar','.gz']
Programs=['.exe','.msi']
currentpath=os.getcwd()
for directory in directorys:
    if not os.path.exists(directory):
        os.mkdir(directory)
for item in os.listdir():
    if os.path.isdir(item):
        if item in directorys:
            pass
        else:
            os.rename(item,os.path.join(currentpath, 'Compressed', item))
    else:
        if os.path.splitext(item)[1] in Images:
            os.rename(item,os.path.join(currentpath, 'Images', item))
        elif os.path.splitext(item)[1] in Videos:
            os.rename(item,os.path.join(currentpath, 'Videos', item))
        elif os.path.splitext(item)[1] in Documents:
            os.rename(item,os.path.join(currentpath, 'Documents', item))
        elif os.path.splitext(item)[1] in Compressed:
            os.rename(item,os.path.join(currentpath, 'Compressed', item))
        elif os.path.splitext(item)[1] in Programs:
            os.rename(item,os.path.join(currentpath, 'Programs', item))
        else:
            os.rename(item,os.path.join(currentpath, 'Others', item))
