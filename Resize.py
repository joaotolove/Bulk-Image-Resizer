import PIL
import os
import os.path
from PIL import Image

reduction_factor = 2 #the higher the factor, the smaller the image.
images_format=['.png', '.jpg'] #Formats that will be resized

for file in os.listdir():
    filename, file_extension = os.path.splitext(file)
    if file_extension in images_format:
        f_img = "result/"+file
        img = Image.open(file)
        img = img.resize((int(img.size[0]/reduction_factor),int(img.size[1]/reduction_factor), 0)
        img.save(f_img)
