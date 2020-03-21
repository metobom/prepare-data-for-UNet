import cv2
import os
import random
from find_threshold import findVal

#To apply this code to your images, all images should be in same extension.
#To make all extension same in your folder you can use simple commands in cmd.
#Careful, this commands does not work in Powershell. Don't know why.
#Command is -> ren *.(INITIAL_EXTENSION) *.(DESIRED_EXTENSION)
#Example -> ren *.jpg *.png (converts all jpg extensions to png)
#Source for this: https://www.youtube.com/watch?v=JCYqLCb7vhY



#THIS CODE is for preparing your image dataset for UNet.
#CAREFUL, your input images must be zerofilled names. Otherwise outputs will not be in order.


def converter(img):
    th = findVal(img)
    for j in range(img.shape[1]):
        for i in range(img.shape[0]):
            if img[i,j] == th: #color value of labelme mask in grayscale
                img[i,j] = 255
    return img

###########main###########


img_path = r'mask_inputs/'
out_path = r'mask_outputs/'

for filename in os.listdir(img_path):
    if filename.endswith(".png"):
        print(filename)
        img = cv2.imread(img_path + filename,0)
        cv2.imwrite((out_path + filename), converter(img))
    else:
        print('Could not find files with expected extension.')












