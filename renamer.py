#To apply this code to your images, all images should be in same extension.
#To make all extension same in your folder you can use simple commands in cmd.
#Careful, this commands does not work in Powershell. Don't know why.
#Command is -> ren *.(INITIAL_EXTENSION) *.(DESIRED_EXTENSION)
#Example -> ren *.jpg *.png (converts all jpg extensions to png)
#Source for this: https://www.youtube.com/watch?v=JCYqLCb7vhY


#THIS CODE is for changing file names in a folder like 0.(YOUR_EXTENSION), 1.(YOUR_EXTENSION)...
#CAREFUL, there is no output folder for this. So save your images to somewhere if needed.

import os
path = r'rename_inputs'
files = os.listdir(path)

def renamer_foo(files, path):
    for index, file in enumerate(files):
        #put your extension to '.png' part.
        os.rename(os.path.join(path, file), os.path.join(path, '00' + ''.join([str(index),'.png',])))# '00' is zerofill 

#main
renamer_foo(files, path)
