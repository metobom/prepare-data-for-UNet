#This code finds th value to use in prepare_mask.py
import cv2
import numpy as np

def findVal(img):
    out = np.max(img)
    return out
    
    

