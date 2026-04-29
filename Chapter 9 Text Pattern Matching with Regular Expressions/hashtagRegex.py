#Chapter 9 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter9.html

import re
def get_hashtags(sentence):
    hashtag_regex = re.compile(r"#\w+")
    return hashtag_regex.findall(sentence)
    

print("Enter a sentence:")
user_input = input()
results = get_hashtags(user_input)
for result in results:
    print(result)