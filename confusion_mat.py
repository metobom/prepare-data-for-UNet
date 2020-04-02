import os
import cv2
import numpy as np


'''
To use this, you need to go test_imgs.py and change output path to data/test/test_outs/ and create test_masks folder inside data folder.
1- Use test_imgs.py get predicted images.
2- Put your labelled masks to data/test_masks/ that you just created.
3- Run this code.

CAREFUL: THIS CODE IS FOR ONLY BINARY BLACK/WHITE CLASSIFICATION.
'''


def confusion_mat():
    #vars
    tp, fn, tn, fp = 0,0,0,0
    mask_path = r'data/test_masks/'
    pred_path = r'data/test/test_outs/'
    a = np.array([])
    b = np.array([])
  
    #read predicts and flat
    for filename in os.listdir(pred_path):
        if filename.endswith('.png'):
            img = cv2.imread(pred_path+filename,0)
            flat_img = img.reshape(-1)
            #fix non binary pixels
            for i in range(len(flat_img)):
                if flat_img[i] >0:
                    flat_img[i] = 255
                else:
                    flat_img[i] = 0
            a = np.concatenate([a, flat_img])
    #print(a.shape)
      
    #read true masks and flat
    for filename in os.listdir(mask_path):
        if filename.endswith('.png'):
            mask = cv2.imread(mask_path+filename,0)
            flat_mask = mask.reshape(-1)
        b = np.concatenate([b,flat_mask])
    #print(b.shape)



    #create confusion mat
    for j in range(len(a)):#or len(flat_mask)
        if a[j] == 255 and b[j] == 255:
            tp+=1
        if a[j] == 255 and b[j] == 0:
            fn+=1
        if a[j] == 0 and b[j] == 0:
            tn+=1
        if a[j] == 0 and b[j] == 255:
            fp+=1
    #calculate acc
    acc = (tp+tn)/(tp+tn+fp+fn)
    print(acc*100)

#MAIN
confusion_mat()






