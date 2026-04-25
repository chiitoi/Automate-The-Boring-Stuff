spam = ['apples', 'bananas', 'tofu', 'cats']
one = ['apples']
empty = []
def comma_code(items):
    if not items:
        return "The list must have at least one item."
    
    if len(items) == 1:
        return items[0]

    return ", ".join(items[:-1]) + ", and " + items[-1]

print(comma_code(spam))
print(comma_code(one))
print(comma_code(empty))