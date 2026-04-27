#Chapter 6 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter6.html

sentence1 = "The quick brown fox jumps over the yellow lazy dog."
sentence2 = "Hello, world!"

alphabet = "qwertyuiopasdfghjklzxcvbnm"

#The function determines if all the letters of the alphabet were used in the string (aka a pangram) by utilizing a set.
def is_pangram(sentence):
    letters = set()
    for letter in sentence:
        if letter.lower() in alphabet:
            letters.add(letter.lower())
    return len(letters) == 26

print(is_pangram(sentence1))
print(is_pangram(sentence2))