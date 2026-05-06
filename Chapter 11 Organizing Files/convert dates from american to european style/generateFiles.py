#Helper script to create valid American style date text files so that convertDateStyles.py can convert them to European style
import random
file_list = set()
gibberish_prefix = ('spam', 'egg', 'bacon', 'chicken', 'spam egg bacon', "11-11", '2231', '')
gibberish_suffix = ('hotdog', 'mustard', 'relish', 'onion', 'ketchup', '9999', '')
while len(file_list) < 10:
    month = random.randint(1,12)
    year = random.randint(1971, 2026)
    if month in (4, 6, 9, 11):
        day = random.randint(1, 30)
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    else:
        day = random.randint(1, 31)
    prefix = random.choice(gibberish_prefix)
    suffix = random.choice(gibberish_suffix)
    file_name = f'{prefix}{month:02}-{day:02}-{year}{suffix}.txt'
    
    if file_name in file_list:
        continue

    print(f'Creating file: {file_name}')
    with open(file_name, 'w') as file:
        pass
    file_list.add(file_name)