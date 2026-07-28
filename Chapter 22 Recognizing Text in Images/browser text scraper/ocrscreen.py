#Chapter 22 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter22.html

import pyautogui, time
import pytesseract as tess

print("Taking a screenshot in 3 seconds...")
time.sleep(3)

# The coordinates for the text portion. Change as needed:
LEFT = 75
TOP = 170
RIGHT = 525
BOTTOM = 1030

# Capture a screenshot:
img = pyautogui.screenshot()

# Crop the screenshot to the text portion:
img = img.crop((LEFT, TOP, RIGHT, BOTTOM))

# Run OCR on the cropped image:
text = tess.image_to_string(img, lang='eng')
print(text)

# Add the OCR text to the end of output.txt:
with open('output.txt', 'a', encoding="UTF-8") as file_obj:
    file_obj.write(text)