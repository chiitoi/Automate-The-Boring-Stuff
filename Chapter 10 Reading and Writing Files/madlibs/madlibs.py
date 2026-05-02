#Chapter 10 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter10.html

from pathlib import Path
import pprint
import string

#get current directory
p = Path.cwd()

#pprint.pprint(list(p.glob("madlib.txt")))

#establish a path to the madlib text file
madlibs_file_path = p / "madlib.txt"

#create a madlib text file with the following madlib if the file doesn't exist
if not madlibs_file_path.exists():
    with open('madlib.txt', 'w', encoding="UTF-8") as file_obj:
        file_obj.write("The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.")

with open(madlibs_file_path, encoding="UTF-8") as file_obj:
    content = file_obj.read()

words = content.split() 
for index, word in enumerate(words):
    #remove any punctuation in the word so that "VERB." just becomes "VERB"
    clean_word = word.strip(string.punctuation)

    if clean_word in ("ADJECTIVE", "NOUN", "VERB"):
        article = 'an' if clean_word == 'ADJECTIVE' else 'a'
        print(f"Enter {article} {clean_word.lower()}:")
        user_input = input()
        
        #add the puncuation back at the end of the word
        words[index] = user_input + word[len(clean_word):]

print(" ".join(words))