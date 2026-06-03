#Chapter 18 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter18.html

import csv

csv_file = open('fizzBuzz.csv', 'w', newline='')
output_writer = csv.writer(csv_file)

results = []
for i in range(1, 10001):
    print(i)
    if i % 5 == 0 and i % 3 == 0:
        result = 'Fizz Buzz'
    elif i % 3 == 0:
        result = 'Fizz'
    elif i % 5 == 0:
        result = 'Buzz'
    else:
        result = str(i)
    
    results.append(result)
    if len(results) == 10:
        output_writer.writerow(results)
        results = []

csv_file.close()