#Chapter 22 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter22.html

import os, json
import pytesseract as tess
from PIL import Image

image_dictionary = {}

for file in os.listdir():
    if not file.endswith('.png'):
        continue

    img = Image.open(file)
    double_sized_img = img.resize((img.width * 2, img.height * 2))

    text = tess.image_to_string(double_sized_img)
    print(text)
    image_dictionary[file] = text
    
with open('imageTextEnlarged.json', 'w', encoding='utf-8') as file_obj:
    file_obj.write(json.dumps(image_dictionary, indent=2))