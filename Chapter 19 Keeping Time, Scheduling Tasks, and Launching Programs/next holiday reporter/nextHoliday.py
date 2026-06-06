#Chapter 19 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter19.html

import datetime

def next_holiday(from_date):
    holidays = {"October 31": "Halloween", "February 14": "Valentine's Day", "April 1": "April Fool's Day", "May 1": "May Day", "May 5": "Cinco de Mayo"}
    one_day = datetime.timedelta(days=1)
    while True:
        month = from_date.strftime('%B')
        day = from_date.strftime('%d')
        month_day = f'{month} {day.lstrip('0')}'
        if month_day in holidays:
            return holidays[month_day]
        from_date += one_day
        
print(next_holiday(datetime.datetime(2028, 10, 31, 0, 0, 0)))
print(next_holiday(datetime.datetime(3000, 1, 1, 0, 0, 0)))
print(next_holiday(datetime.datetime.now()))