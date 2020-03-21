import cv2
import os
import random

#To apply this code to your images, all images should be in same extension.
#To make all extension same in your folder you can use simple commands in cmd.
#Careful, this commands does not work in Powershell. Don't know why.
#Command is -> ren *.(INITIAL_EXTENSION) *.(DESIRED_EXTENSION)
#Example -> ren *.jpg *.png (converts all jpg extensions to png)
#Source for this: https://www.youtube.com/watch?v=JCYqLCb7vhY


 
img_path = r'preprocess_inputs/'
out_path = r'preprocess_outputs/'


for filename in os.listdir(img_path):
    if filename.endswith(".png"):
        print(filename)
        img = cv2.imread(img_path + filename,0)
        img_out = cv2.equalizeHist(img)
        img_out = cv2.GaussianBlur(img_out, (5,5),0)
        cv2.imwrite(out_path + filename, img_out)
    else:
        print('Could not find files with expected extension.')












