#Chapter 8 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter8.html

import time

character_length = 100

while True:
    for i in range(character_length):
        print("0"*i + "."*(character_length-i))
        time.sleep(0.01)
    for i in range(character_length):
        print("."*i + "0"*(character_length-i))
        time.sleep(0.01)