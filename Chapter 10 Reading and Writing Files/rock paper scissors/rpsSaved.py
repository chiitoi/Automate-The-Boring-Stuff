#Chapter 10 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter10.html

import random, sys, shelve

print('ROCK, PAPER, SCISSORS')

#open a shelf file to access data from previous games
with shelve.open('rps_data') as shelf_file:

    #check to see if each key exists in the file, if not we initialize it
    for key in ('wins', 'losses', 'ties'):
        if key not in shelf_file:
            shelf_file[key] = 0

    wins = shelf_file['wins']
    losses = shelf_file['losses']
    ties = shelf_file['ties']

    while True:
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True:
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            player_move = input('>')
            if player_move == 'q':
                sys.exit()  # Quit the program.
            if player_move == 'r' or player_move == 'p' or player_move == 's':
                break  # Break out of the player input loop.
            print('Type one of r, p, s, or q.')

        # Display what the player chose:
        if player_move == 'r':
            print('ROCK versus...')
        elif player_move == 'p':
            print('PAPER versus...')
        elif player_move == 's':
            print('SCISSORS versus...')

        # Display what the computer chose:
        move_number = random.randint(1, 3)
        if move_number == 1:
            computer_move = 'r'
            print('ROCK')
        elif move_number == 2:
            computer_move = 'p'
            print('PAPER')
        elif move_number == 3:
            computer_move = 's'
            print('SCISSORS')

        # Display and record the win/loss/tie:
        if player_move == computer_move:
            print('It is a tie!')
            ties = ties + 1
        elif player_move == 'r' and computer_move == 's':
            print('You win!')
            wins = wins + 1
        elif player_move == 'p' and computer_move == 'r':
            print('You win!')
            wins = wins + 1
        elif player_move == 's' and computer_move == 'p':
            print('You win!')
            wins = wins + 1
        elif player_move == 'r' and computer_move == 'p':
            print('You lose!')
            losses = losses + 1
        elif player_move == 'p' and computer_move == 's':
            print('You lose!')
            losses = losses + 1
        elif player_move == 's' and computer_move == 'r':
            print('You lose!')
            losses = losses + 1

        #save the results after a round
        shelf_file['wins'] = wins
        shelf_file['losses'] = losses
        shelf_file['ties'] = ties