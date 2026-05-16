#Chapter 6 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter6.html

spam = ['apples', 'bananas', 'tofu', 'cats']
one = ['apples']
two = ['apples', 'bananas']
empty = []

#This function returns the list of items into a string. If the list contains more than one item it adds  ", and" to the string 
def comma_code(items):
    if not items:
        return "The list must have at least one item."
    
    if len(items) == 1:
        return items[0]

    return ", ".join(items[:-1]) + ", and " + items[-1]

print(comma_code(spam))
print(comma_code(one))
print(comma_code(two))
print(comma_code(empty))