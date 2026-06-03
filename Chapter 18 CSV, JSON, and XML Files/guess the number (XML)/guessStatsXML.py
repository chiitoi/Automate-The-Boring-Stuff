#Chapter 18 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter18.html

# This is a guess the number game.
import random, os
import xml.etree.ElementTree as ET

filename = 'guessStats.xml'

#check if the XML file exists, if not create a new tree
if os.path.exists(filename):
    #open in append mode
    with open(filename, 'r', encoding='utf-8') as file_obj:
        stats = ET.fromstring(file_obj.read())
else:
    stats = ET.Element('stats')

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

#create a new game element and add it to the stats element
game_element = ET.SubElement(stats, 'game')

#add the secret_number attribute to the game element
game_element.set('secret_number', str(secret_number))

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input('>'))

    #add each guess as a separate element within the game element
    guess_element = ET.SubElement(game_element, 'guess')
    guess_element.text = str(guess)

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
    #set the won attribute for the "game" element
    game_element.set('won', 'True')
else:
    print('Nope. The number was ' + str(secret_number))
    game_element.set('won', 'False')


#write game results to XML file
with open(filename, 'w', encoding='utf-8') as file_obj:
    ET.indent(stats, space='\t')
    file_obj.write(ET.tostring(stats, encoding='unicode'))
    
"""
<stats>
    <game secret_number="4" won="True">
        <guess>10</guess>
        <guess>5</guess>
        <guess>6</guess>
        <guess>9</guess>
        <guess>3</guess>
        <guess>4</guess>
    </game>
    <game secret_number="12" won="False">
        <guess>2</guess>
        <guess>4</guess>
        <guess>5</guess>
        <guess>6</guess>
        <guess>8</guess>
        <guess>10</guess>
    </game>
</stats>
"""