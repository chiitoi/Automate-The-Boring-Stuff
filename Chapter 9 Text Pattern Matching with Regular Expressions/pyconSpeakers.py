#Chapter 9 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter9.html

import re
import pprint

placeholder = """
    Ayan Mukhopadhyay 1
    Ayaz Amlani 1
    Aylen Bombelli 1
    Ayman Boustati 1
    Aymeric Augustin 5
    Aysin Oruz 1
    Ayun Daywhea 1
    Ayush Bharti 1
    Ayush Singh 2
    Azalee Bos 4
    Azan Bin Zahid 1
    Azhar Desai 1
    Azucena González Muiño 1
    Azzurra Ragone 1
    B. Cannon 1
    B. Warsaw 1
    Babak Khataee 1
    Babila Lima 1
    Bae Doo-sik 1
    배준현 2
    Baek Seung-hoon 1
    Baekjin Kim 1
    박찬성 1
    박현우 1
    박종현 1
    박중석 1
    Bagrat Amirbekian 1
    Baharan Mirzasoleiman 1
    Baiju Muthukadan 1
    Baiju Muthukaden 1
"""

speakers = placeholder.splitlines()
print(speakers)
new_list = []
#split the data by grabbing the name, the space between, and the number
#replace the string so that we just have {Name},{Number}
speaker_regex = re.compile(r"\s+(.*)\s(\d+)")
for item in speakers:
    results = speaker_regex.findall(item)
    new_string = speaker_regex.sub(r"\1,\2", item)
    new_list.append(new_string)


pprint.pprint(new_list)
