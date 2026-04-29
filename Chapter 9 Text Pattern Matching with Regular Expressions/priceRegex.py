#Chapter 9 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter9.html

import re

def get_price(sentence):
    price_regex = re.compile(r"\$\d+(?:\.\d{2})?")
    return price_regex.findall(sentence)

sales_pitch1 = "It was $5.99 but is now on sale for $5.95!!"
sales_pitch2 = "Previous it was $6.60 but now it's on sale for $6!!!!!"
print(get_price(sales_pitch1))
print(get_price(sales_pitch2))