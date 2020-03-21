# prepare-data-for-UNet
This repo contains how I prepared my data for zhixuhao's UNet implemention

zhixuhao's implemention: https://github.com/zhixuhao/unet

# Tutorial for prepare_mask
I masked my images with labelme (polygonal). You can find how to use labelme in labelme repo's tutorial part.
After you git clone labelme repo to your computer you just need to type 'labelme' in Windows PowerShell to execute program.

1- After you finish labelling your images labelme outputs color mask. But UNet takes binary mask as input.

2- To get binary masks put your color masks to mask_inputs folder. Then run prepare_masks.py file. (Careful, images should be like 000, 001, .... otherwise outputs won't be in order. You can use renamer.py to do this.)

3- Outputs will be in mask_outputs folder. 

4- I put some images to mask_inputs for you to test.

labelme: https://github.com/wkentaro/labelme

# Tutorial for renamer
This file is for renaming each image in a folder.

1- Put your images to renamer inputs and run the code. Careful, outputs will ve overwritten to your inputs in same folder.

# Tutorial for preprocess
This file is specific for my data. My data was pretty low quality and dirty. To get good outputs I used equalizeHist method and blurred images. As output I get the patterns I wanted. You should play with this file for your dataset.

1- Put your images to preprocess_inputs. Outputs will be in preprocess_outputs.

# Data augmentation 
I used zhixuhao's augmentation code. But I changed parameteres for my data.

# Finally...
Remember all your images must be in same size. After getting clear input images and binary mask you are good to go to train your data.
NOTE: I had 34 images. With augmentation I had 68 images to train. Check out my repos for UNet (not completed)  

NOT: Eğer İngilizce sıkıntısı çekiyorsanız Türkçe olarak bir issue açabilirsiniz.
