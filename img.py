from PIL import Image
from fractions import Fraction as frac
import os
import json
import time
#
# try:
# 	data_file = open('', 'r+')
# 	data = json.load(data_file)
# except IOError as e:
# 	print(e)
#
# img = Image.open("/Users/katiechen/Desktop/portfolio/korea/public/images/IMG_20200118_160102.jpg")._getexif()
#
# date_created = img[36867]
#
# print(time.strptime(date_created, "%Y:%m:%d %H:%M:%S"))


list = []
for (root,dir,file) in os.walk('/Users/katiechen/Desktop/portfolio/korea/public/images'):
    for files in file:
        if files != ".DS_Store" and files != "16-02-2020 at 01.39.10img 1.JPG":
            w,h = Image.open(os.path.join(root,files)).size
            width = frac(w,h).numerator
            height = frac(w,h).denominator
            exif_data = Image.open(os.path.join(root, files))._getexif()
            exif_date = exif_data[36867]
            list.append({
            "src": os.path.join(root, files),
            "width": width,
            "height": height,
            "date_created": exif_date
            })


list.sort(key=lambda i: time.strptime(i["date_created"], "%Y:%m:%d %H:%M:%S"))
index = 0

for i in list:
    i.update({"index": index})
    index = index + 1

with open("/Users/katiechen/Desktop/portfolio/korea/src/components/photo.json", "r+") as data_file:
    json.dump(list, data_file, indent=4, sort_keys=True)
