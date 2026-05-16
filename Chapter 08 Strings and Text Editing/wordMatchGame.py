#Chapter 8 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter8.html

import random
word_list = 'MITTS FLOAT BRICK LIKED DWARF COMMA GNASH ROOMS UNITE BEARS SPOOL ARMOR'.split()

def get_word_hint(secret_word, guess_word):
    upper_guess = guess_word.upper()
    secret_word = secret_word.upper()

    #Create a string of "xxxxx" by default so that we can insert "O" for correct characters positions and "o" for partially correct guesses 
    result = ["x"] * len(secret_word)

    #Create a list of out of the secret word so that we can remove the correct/partial guesses in cases where guesses contain more than 1 of the same character
    remaining = list(secret_word)

    n = len(secret_word)
    for i in range(n):
        if upper_guess[i] == secret_word[i]:
            result[i] = "O"
            remaining[i] = None

    for i in range(n):
        if result[i] == "x" and upper_guess[i] in remaining:
            result[i] = "o"
            remaining[remaining.index(upper_guess[i])] = None

    #old logic. If the word was "MITTS" and the user guessed "mmmmm" it would return "Ooooo" instead of "Oxxxx"
    '''
    for i in range(len(secret_word)):
        if secret_word[i] == upper_guess[i]:
            guess_attempt += "O"
        elif upper_guess[i] in secret_word:
            guess_attempt += "o"
        else:
            guess_attempt += "x"
    '''
    
    return "".join(result)

def totally_not_wordle(words):
    secret_word = random.choice(words)
    print("Guess the secret five-letter word:")

    for _ in range(6):
        #prompts the user to continue entering a word until it's a 5 letter alphabet word only, no numbers or symbols
        while True:
            user_guess = input()
            user_guess = user_guess.strip()
            if not user_guess.isalpha():
                print("Please only enter alphabet letters")
            elif not len(user_guess) == 5:
                print("Please enter a 5 letter word")
            else:
                break
        
        #break out of the function early if the guess is correct
        if user_guess.upper() == secret_word:
            print()
            print(f"You got it! The secret word is: {secret_word}")
            return

        hint = get_word_hint(secret_word, user_guess)
        print(hint)
        print()

    print(f"The secret word was {secret_word}. Better luck next time.")
        
totally_not_wordle(word_list)