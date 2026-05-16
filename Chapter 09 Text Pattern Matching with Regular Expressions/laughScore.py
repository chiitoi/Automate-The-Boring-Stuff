#Chapter 9 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter9.html

import re

def laugh_score(laugh):
    laugh_regex = re.compile(r"ha[ha]*",re.I)
    result = laugh_regex.search(laugh)
    if result:
        return len(result.group())
    else:
        return 0

assert laugh_score('abcdefg') == 0
assert laugh_score('h') == 0
assert laugh_score('ha') == 2
assert laugh_score('HA') == 2
assert laugh_score('hahaha') == 6
assert laugh_score('ha ha ha') == 2
assert laugh_score('haaaaa') == 6
assert laugh_score('ahaha') == 4
assert laugh_score('Harry said Hahaha') == 2
