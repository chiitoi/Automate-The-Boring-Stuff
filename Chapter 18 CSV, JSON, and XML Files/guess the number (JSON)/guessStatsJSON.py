#Chapter 18 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter18.html

# This is a guess the number game.
import random, json, os

#check if the json file exists, if not create a new file
if os.path.exists('guessStats.json'):
    #open the file
    with open('guessStats.json', 'r', encoding='utf-8') as file_obj:
        stat_record = json.load(file_obj)
else:
    #create a new one
    stat_record = []

#keep track of guesses
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

game_stat = {'Secret Number': secret_number, 'Guesses': [], 'Won': False}

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input('>'))
    game_stat['Guesses'].append(guess)

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
    game_stat['Won'] = True
else:
    print('Nope. The number was ' + str(secret_number))

stat_record.append(game_stat)

#write game results to json file
with open('guessStats.json', 'w', encoding='utf-8') as file_obj:
    file_obj.write(json.dumps(stat_record))

"""
[
    {"Secret Number": 18,
    "Guesses": [10, 15, 18],
    "Won": true},
    
    {"Secret Number": 14,
    "Guesses": [10, 14],
    "Won": true},
    
    {"Secret Number": 14,
    "Guesses": [2, 4, 5, 7, 8, 9], 
    "Won": false}]
"""