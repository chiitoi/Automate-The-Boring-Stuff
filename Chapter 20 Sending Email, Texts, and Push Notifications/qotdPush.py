#Chapter 20 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter20.html

import requests, random, datetime, sys
from pathlib import Path

#if qotdLastSent.txt doesn't exist then create a blank file
if not Path('qotdLastSent.txt').exists():
    with open('qotdLastSent.txt', 'w', encoding='utf-8') as file_obj:
        pass  #just create the file

current_date = str(datetime.date.today())

#check if a notification has already been sent today
with open('qotdLastSent.txt', encoding='UTF-8') as f:
    logs = f.read()
if current_date in logs:
    print('Email already sent today. Exiting . . .')
    sys.exit()

#get all the quotes
with open('qotd.txt', encoding='UTF-8') as f:
    quotes = f.readlines()

#get the recipient
with open('topic.txt', encoding='UTF-8') as f:
    RECIPIENT = f.read().strip()

random_quote = random.choice(quotes).strip()

requests.post(RECIPIENT, random_quote)
print(f'Notification sent to {RECIPIENT} with the following quote:\n\t{random_quote}')

#record the date and quote
with open('qotdLastSent.txt', 'a', encoding='UTF-8') as f:
    f.write(f'{current_date} {RECIPIENT} {random_quote}')