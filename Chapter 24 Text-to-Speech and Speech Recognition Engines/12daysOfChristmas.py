#Chapter 24 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter24.html

import pyttsx3, time

def speak(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

verses = ['And a partridge in a pear tree.', 'Two turtle doves,',
'Three French hens,', 'Four calling birds,', 'Five gold rings,',
'Six geese a-laying,', 'Seven swans a-swimming,', 'Eight maids a-milking,',
'Nine ladies dancing,', 'Ten lords a-leaping,', 'Eleven pipers piping,',
'Twelve drummers drumming,']

day_count = 0
for day in days:
    speak(f'On the {day} day of Christmas, my true love gave to me')
    if day == 'first':
        speak('A partridge in a pear tree,') 
    else:
        for day_index in range(day_count, -1, -1):
            speak(verses[day_index])
    day_count += 1
    time.sleep(2)
    