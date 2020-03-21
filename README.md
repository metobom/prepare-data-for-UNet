# prepare-data-for-UNet
This repo contains how I prepared my data for zhixuhao's UNet implemention

zhixuhao's implemention: https://github.com/zhixuhao/unet

# Tutorial
I masked images with labelme. You can find how to use labelme in labelme repo's tutorial part.
After you git clone labelme repo to your computer you just need to type 'labelme' in Windows PowerShell to execute program.

1- After you finish labelling your images labelme outputs color mask. But UNet takes binary mask as input.

2- Put your color masks to inputs folder. Then run prepare_masks.py file.

3- Outputs will be in outputs folder.

4- If you need to change masks names like 0, 1, 2... just run renamer.py after you complete converting.

5- Now your data is ready to put UNet.

NOT COMPLETED

labelme: https://github.com/wkentaro/labelme
