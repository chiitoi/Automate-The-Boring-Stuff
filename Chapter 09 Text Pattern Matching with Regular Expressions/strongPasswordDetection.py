#Chapter 9 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter9.html

import re
contains_uppercase_regex = re.compile(r'[A-Z]')
contains_lowercase_regex = re.compile(r'[a-z]')
contains_digit_regex = re.compile(r'\d')

def strong_password_detection(password):
    if len(password) < 8:
        return False, "Your password must be at least 8 characters long."

    if not contains_uppercase_regex.search(password):
        return False, "Your password must contain at least 1 uppercase character."
    
    if not contains_lowercase_regex.search(password):
        return False, "Your password must contain at least 1 lowercase character."
    
    if not contains_digit_regex.search(password):
        return False, "Your password must contain at least 1 digit."

    return True, "You have a strong password."

short_password = "pass"
weak_password = "password"
strong_password = "PaSswoRD123"

result, message = strong_password_detection(weak_password)
print(result, message)

result, message = strong_password_detection(strong_password)
print(result, message)