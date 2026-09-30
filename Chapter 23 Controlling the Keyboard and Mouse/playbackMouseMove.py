#Chapter 23 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter23.html

import json, pyautogui

with open('mousePositions.json', encoding='utf-8') as file_obj:
    positions = json.loads(file_obj.read())

for position in positions:
    pyautogui.moveTo(position[0], position[1])
    pyautogui.sleep(0.1)