#Chapter 8 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter8.html


def spongecase(text):
    text_list = list(text)
    is_uppercase = False
    
    for i, letter in enumerate(text_list):
        if letter.isalpha():
            text_list[i] = letter.upper() if is_uppercase else letter.lower()
            is_uppercase = not is_uppercase
    return "".join(text_list)

print("Enter a sentence:")
sentence = input()

print(spongecase(sentence))