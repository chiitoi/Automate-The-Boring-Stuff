#Chapter 12 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter12.html

# This is a guess the number game from Chapter 3 but with the print/input statements replaced with pymsgbox functions.
import random, pymsgbox

secret_number = random.randint(1, 20)
pymsgbox.alert('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    guess = int(pymsgbox.prompt('Take a guess.'))

    if guess < secret_number:
        pymsgbox.alert('Your guess is too low.')
    elif guess > secret_number:
        pymsgbox.alert('Your guess is too high.')
    else:
        break  # This condition is the correct guess!

if guess == secret_number:
    pymsgbox.alert('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    pymsgbox.alert('Nope. The number was ' + str(secret_number))