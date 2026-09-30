#Chapter 23 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter23.html

import pyautogui

try:
    while True:
        pyautogui.move(1, 0, duration=0.1)
        pyautogui.sleep(10)
        pyautogui.move(-1, 0, duration=0.1)
        pyautogui.sleep(10)
except KeyboardInterrupt:
    pass