# -*- coding: UTF-8 -*-
import time, os, shutil, sys
from PIL import Image

path = os.getcwd()
accepted_folder = "Accepted"
rejected_folder = "Rejected"

print(path)

def extractor():
    for images in os.listdir():
        
        if os.name == "posix":
            full_image_path = path + "/" + str(images)
        elif os.name == "nt":
            full_image_path = path + str("\\") + str(images)
        else:
            print("Unknow OS")
        
        if not os.path.exists(accepted_folder):
            os.makedirs(accepted_folder)
        
        if not os.path.exists(rejected_folder):
            os.makedirs(rejected_folder)

        if images.endswith(".py"):
            continue
        
        img = Image.open(images)
        #print(img.size[0], "x" ,img.size[1])
        
        if img.size[0] > img.size[1]:
            print("{} <- Rejected.".format(images))
            img.close()
            shutil.move(full_image_path, rejected_folder)
        else:
            print("{} <- Accepted.".format(images))
            img.close()
            shutil.move(full_image_path, accepted_folder)
        
    if os.name == "posix":
        os.system("sudo chmod 777 -R Accepted/")
        os.system("sudo chmod 777 -R Rejected/")
        print("Fixing permissions.")
        
if __name__ == "__main__":
    extractor()
