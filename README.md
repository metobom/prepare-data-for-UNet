# prepare-data-for-UNet
This repo contains how I prepared my data for zhixuhao's UNet implemention
NOT: Eğer İngilizce sıkıntısı çekiyorsanız Türkçe olarak bir issue açabilir ya da bana mail atabilirsiniz. metobomm@gmail.com

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

1- Git clone zhixuhao's unet repo. (https://github.com/zhixuhao/unet)

2- Create a path for your images, labels, tests and augmentations inside data folder. (You can delete membrane if you won't train that dataset)

3- Put your images to image path, masks to label path, test images to test path and left augmentation path empty.

4- Go to dataPrepare.ipynb (convert it to .py file if you don't like notebook.) and specify your paths.

5- Run the notebook. Outputs will be in your augment path. Split images and masks to your image and mask paths again.

# Training 

1- In zhixuhao's repo, open trainUnet.ipynb (convert it to .py file if you don't like notebook) and specify your paths.

2- Again in same notebook specify your batch size, steps, epoch and weight file name. Weight file should be in .hdf5 format.

3- Run the notebook cell by cell. After training completed in last cell you can test your weights. Test outputs will be in folder that you specified. I put test_imgs.py to my repo. You can test your weights with it too.

# Finally...
Remember all your images must be in same size. Also I was keep getting full gray, black or wrong outputs. I solved it by preprocessing and increasing my image number by 5 (29 to 34). You can see one of my test results in my repo.

