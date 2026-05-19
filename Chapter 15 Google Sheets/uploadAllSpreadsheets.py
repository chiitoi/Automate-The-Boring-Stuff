#Chapter 15 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter15.html

import ezsheets, os

for filename in os.listdir('.'):
    if filename.endswith('.xlsx') or filename.endswith('.csv'):
        print(f'Uploading {filename}...')
        ss = ezsheets.upload(filename)