#Chapter 23 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter23.html

import pyautogui, pyperclip

windows = pyautogui.getWindowsWithTitle('Notepad')
if windows:
    notepad_window = windows[0]

    if notepad_window.isMinimized:
        notepad_window.restore()
    notepad_window.activate()
    pyautogui.sleep(0.5)

    pyautogui.click(notepad_window.left + 100, notepad_window.top + 100)
    pyautogui.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.3)

    clipboard = pyperclip.paste()
    print(clipboard)
else:
    print('Notepad not found.')