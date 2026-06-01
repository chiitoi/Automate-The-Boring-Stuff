#Chapter 17 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter17.html

# This is a guess the number game.
import random, docx
from pathlib import Path

if Path('guessWordLog.docx').exists():
    doc = docx.Document('guessWordLog.docx')
else:
    doc = docx.Document()

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
doc.add_paragraph('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    doc.add_paragraph('Take a guess.')
    guess = int(input('>'))
    doc.add_paragraph(f'>{guess}')

    if guess < secret_number:
        print('Your guess is too low.')
        doc.add_paragraph('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
        doc.add_paragraph('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
    doc.add_paragraph('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))
    doc.add_paragraph('Nope. The number was ' + str(secret_number))

doc.save('guessWordLog.docx')
