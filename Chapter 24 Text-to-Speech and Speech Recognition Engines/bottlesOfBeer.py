#Chapter 24 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter24.html

import pyttsx3

#moving the engine initiation line outside of the function causes the speech to stop on my setup
def speak(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

bottles = 3
while bottles > 0:
    speak(f"""{bottles} bottle{"s" if bottles > 1 else ''} of beer on the wall,
{bottles} bottle{"s" if bottles > 1 else ''} of beer,
Take one down, pass it around,""")
    bottles -= 1
    if bottles > 0:
        speak(f'{bottles} bottle{"s" if bottles > 1 else ''} of beer on the wall.')

speak('No more bottles of beer on the wall.')