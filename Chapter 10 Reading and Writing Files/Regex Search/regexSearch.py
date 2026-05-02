#Chapter 10 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter10.html

from pathlib import Path
import re
import pprint
print("Enter a regex expression:")
user_input = input()

try:
    user_regex = re.compile(user_input)
except re.error as e:
    print(f"Invalid regex: {e}")
    exit()

p = Path.cwd()
text_files = list(p.glob("*.txt"))

for file in text_files:
    with open(file, encoding="UTF-8") as file_obj:
        content = file_obj.read()
    results = user_regex.findall(content)
    print(f"\nFile: {file.name}")
    pprint.pprint(results)