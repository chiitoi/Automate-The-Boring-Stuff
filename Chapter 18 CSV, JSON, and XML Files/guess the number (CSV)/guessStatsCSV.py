#Chapter 18 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter18.html

# This is a guess the number game.
import random, csv, os

#check if the csv file exists, if not create a new file
if os.path.exists('guessStats.csv'):
    #open in append mode
    csv_file = csv.writer(open('guessStats.csv', 'a', newline=''))
else:
    csv_file = csv.writer(open('guessStats.csv', 'w', newline=''))
    csv_file.writerow(['Secret Number', 'Won', 'Attempts', 'Guess 1', 'Guess 2', 'Guess 3', 'Guess 4', 'Guess 5', 'Guess 6'])

#keep track of guesses
guesses = []

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input('>'))
    guesses.append(guess)

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

won_game = False

if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
    won_game = True
else:
    print('Nope. The number was ' + str(secret_number))

#write game results to csv file
csv_file.writerow([secret_number, won_game, guesses_taken] + guesses)

"""
Secret Number,Won,Attempts,Guess 1,Guess 2,Guess 3,Guess 4,Guess 5,Guess 6
15,True,2,10,15
16,True,4,10,15,18,16
8,False,6,1,2,3,4,5,20
"""