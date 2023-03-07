import os
from PIL import Image
import time

imagePath = "./images/"
dir_list = os.listdir(imagePath)


for image in dir_list:
    print("Opening image ", image )
    with Image.open(imagePath + image) as img:
        img.show()
        time.sleep(1)
        img.close()
