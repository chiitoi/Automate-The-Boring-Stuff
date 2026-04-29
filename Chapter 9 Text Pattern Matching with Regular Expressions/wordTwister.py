#Chapter 9 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter9.html

import re
pattern = re.compile(r'\b(\w*)(\w)\b')
print(pattern.sub(r'\2\1', 'Hello world! How are you? I am fine.'))