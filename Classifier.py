# -*- coding: UTF-8 -*-
import time, os, shutil, sys
from PIL import Image

path = os.getcwd()
new_folder_name = "Accepted"

def extractor():
    for images in os.listdir():
        full_image_path = path + str("\\") + str(images)

        if not os.path.exists(new_folder_name):
            os.makedirs(new_folder_name)

        if images.endswith(".py"):
            continue
        
        img = Image.open(images)
        #print(img.size[0], "x" ,img.size[1])
        
        if img.size[0] > img.size[1]:
            print("{} <- Rejected.".format(images))
            img.close()
        else:
            print("{} <- Accepted.".format(images))
            img.close()
            shutil.move(full_image_path, new_folder_name)

if __name__ == "__main__":
    extractor()