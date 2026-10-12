#Chapter 24 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter24.html

import pyttsx3

def speak(text, id_number):
    engine = pyttsx3.init()
    print(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[id_number].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak('Knock knock.', 0)
speak("Who's there?", 1)
speak('Lettuce.', 0)
speak('Lettuce who?', 1)
speak("Lettuce in, it's cold out here!", 0)