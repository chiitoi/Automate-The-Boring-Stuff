#Chapter 6 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter6.html

import random
number_of_streaks = 0
coins = ['H', 'T']
streaks = [['H', 'H', 'H', 'H', 'H', 'H'], ['T', 'T', 'T', 'T', 'T', 'T']]

for experiment_number in range(10000):  # Run 10,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    coin_flips = []
    streak = False
    for i in range(100):
        coin_flips.append(coins[random.randint(0, 1)])

    for i in range(95):
        if coin_flips[i:i+6] in streaks:
            streak = True
            break

    if streak:
       number_of_streaks += 1

    # Code that checks if there is a streak of 6 heads or tails in a row
print('Chance of streak: %s%%' % (number_of_streaks / 100))