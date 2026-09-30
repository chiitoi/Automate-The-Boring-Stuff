#Chapter 23 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter23.html

import pyautogui, json
positions = []
print("Recording mouse positions. Press ctrl-C to quit.")

try:
    while True:
        positions.append(pyautogui.position())
        pyautogui.sleep(0.1)
except KeyboardInterrupt:
    with open('mousePositions.json', 'w', encoding='utf-8') as file_obj:
        file_obj.write(json.dumps(positions))
    print(f'Done. {len(positions)} positions recorded.')