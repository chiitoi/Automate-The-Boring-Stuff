#Chapter 9 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter9.html

import re

def regex_strip(sentence, characters = ""):
    if not characters:
        #search full string for leading and ending white spaces.
        #group the middle part of the string and return it.
        #it will always return something even if the string is empty.
        white_space = re.compile(r"^\s*(.*?)\s*$") 
        contains_spaces = white_space.search(sentence)
        return contains_spaces.group(1)
    else:
        #re.escape in case the user passes in arguments like . - or ]
        #adding ^ and $ checks for leading characters and ending characters in the sentence
        #we sub all that out for an empty characters
        custom_characters = re.compile(rf"^[{re.escape(characters)}]+|[{re.escape(characters)}]+$")
        new_sentence = custom_characters.sub("", sentence)
        return new_sentence

string1 = " asodo "
string2 = r",,,,,rrttg]].-\\g.....banrrrana....rrr"
print(regex_strip(string1))
print()
arguments = ",.grt.]-\\"
print(regex_strip(string2, arguments))