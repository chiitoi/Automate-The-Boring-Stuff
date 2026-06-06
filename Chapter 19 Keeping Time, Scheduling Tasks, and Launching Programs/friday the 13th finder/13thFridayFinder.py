#Chapter 19 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter19.html

import datetime, math

def find_future_friday_the_13th(limit=math.inf):
    now = datetime.datetime.now()
    one_day = datetime.timedelta(days=1)
    dates_found = 0
    while dates_found < limit:
        if now.isoweekday() == 5 and now.day == 13:
            print(now.strftime("%B of %Y"))
            dates_found += 1
        now += one_day

def find_past_friday_the_13th(limit=math.inf):
    now = datetime.datetime.now()
    one_day = datetime.timedelta(days=1)
    dates_found = 0
    while True:
        if now.isoweekday() == 5 and now.day == 13:
            print(now.strftime("%B of %Y"))
            dates_found += 1
        
        #stops if it hits the limit or if the date is 1/1/1
        if now.date() == datetime.date(1, 1, 1) or dates_found == limit:
            break
        now -= one_day

#find_future_friday_the_13th(10)
find_past_friday_the_13th()