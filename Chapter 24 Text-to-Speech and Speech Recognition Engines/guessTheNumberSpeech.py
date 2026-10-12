#Chapter 24 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter24.html

# This is a guess the number game.
import random, pyttsx3

#moving the engine initiation line outside of the function causes the speech to stop on my setup
def speak(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

secret_number = random.randint(1, 20)
speak('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    speak('Take a guess.')
    guess = int(input('>'))

    if guess < secret_number:
        speak(f'Your guess, {guess}, is too low.')
    elif guess > secret_number:
        speak(f'Your guess, {guess}, is too high.')
    else:
        break # This condition is the correct guess!

if guess == secret_number:
    speak(f'Good job! You got it in {guesses_taken} guesses!')
else:
    speak(f'Nope. The number was {secret_number}.')
