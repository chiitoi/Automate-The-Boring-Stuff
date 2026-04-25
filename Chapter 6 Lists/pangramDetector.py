sentence1 = "The quick brown fox jumps over the yellow lazy dog."
sentence2 = "Hello, world!"

alphabet = "qwertyuiopasdfghjklzxcvbnm"

def is_pangram(sentence):
    letters = set()
    for letter in sentence:
        if letter.lower() in alphabet:
            letters.add(letter.lower())
    return len(letters) == 26

print(is_pangram(sentence1))
print(is_pangram(sentence2))