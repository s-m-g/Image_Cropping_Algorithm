from PIL import Image
import os
import shutil
import time
import psutil
#cons_left is the starting location of the folder where the images are stored
path=os.path.join(os.getcwd(),"cons_left")
list1 = os.listdir(path)
for images in list1:
    img_path = path+"//"+images 
    #ideal_cropped is the destination folder where the cropped images have to be saved
    new_path = os.path.join(os.getcwd(),"ideal_cropped")
    image = Image.open(img_path)
    #box=(a,b,c,d)
    # P(a,b) are the starting point of x-axis and y-axis respectively
    # P(c,d) are the ending point of x-axis and y-axis respectively
    box = (92, 0, 300, 279)
    cropped_image = image.crop(box)
    cropped_image.save(new_path+"//"+"new"+images)
    cropped_image.show()
    

  