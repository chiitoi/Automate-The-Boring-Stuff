#Chapter 23 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter23.html

import pyautogui, random

windows = pyautogui.getWindowsWithTitle('Paint')
if windows:
    paint_window = windows[0]

    if paint_window.isMinimized:
        paint_window.restore()
    #if the window isn't active then clicking may not cause the initial color click to work because it has to focus on the window first
    paint_window.activate()

    print('Hover the mouse cursor at the top-left corner of the canvas . . .')
    pyautogui.countdown(5)
    left, top = pyautogui.position()
    print(f'\tTop-left corner recorded as ({left}, {top}).')

    print('Hover the mouse cursor at the bottom-right corner of the canvas . . .')
    pyautogui.countdown(5)
    right, bottom = pyautogui.position()
    print(f'\tBottom-right corner recorded as ({right}, {bottom}).')

    #this is configured for a 1920x1080 resolution
    color_coordinates = []
    for row in range(2):
        for column in range(10):
            color_coordinates.append((760 + column*22, 60 + row*22))

    for i in range(30):
        color_x, color_y = random.choice(color_coordinates)
        pyautogui.moveTo(color_x, color_y)
        pyautogui.sleep(0.1)
        pyautogui.click()

        pyautogui.moveTo(random.randint(left, right), random.randint(top, bottom))
        pyautogui.dragTo(random.randint(left, right), random.randint(top, bottom))
else:
    print('Paint is not opened.')


"""
pyautogui.moveTo(760, 60, duration=1)
#pyautogui.moveTo(760, 60)
for i in range(2):
    pyautogui.moveTo(760, 60+i*22)
    pyautogui.click()
    pyautogui.click()
    pyautogui.sleep(0.5)
    for k in range(9):
        pyautogui.move(22, 0, 0.5)
        pyautogui.click()

for coordinate in color_coordinates:
    pyautogui.moveTo(coordinate[0], coordinate[1], 1)
"""




        
        
    