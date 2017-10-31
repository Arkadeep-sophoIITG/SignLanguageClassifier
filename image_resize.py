from PIL import Image
import os

path="dataset/"

for directory in os.listdir(path):
    for file in os.listdir(path+directory):
		basewidth = 76
		img = Image.open(file)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		img.save(file) 