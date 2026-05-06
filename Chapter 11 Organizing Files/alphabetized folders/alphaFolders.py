#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import os, string
from pathlib import Path

def make_alpha_folders(root_folder):
    #string.ascii_uppercase
    #The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.
    alphabet = string.ascii_uppercase
    for char_one in alphabet:
        first_folder = root_folder / char_one
        print(first_folder)

        #commenting out os.makedirs to prevent it from creating 702 empty folders
        #os.makedirs(first_folder)
        for char_two in alphabet:
            second_folder = f'{char_one}{char_two}'
            print(first_folder / second_folder)
            #os.makedirs(first_folder / second_folder)

base_source = Path.cwd()

make_alpha_folders(base_source)