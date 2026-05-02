#Chapter 10 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter10.html

def write_zigzag(indent_limit, asterisks, line_limit):
    if indent_limit < 2:
        print("Your indent space must be greater than 1")
        return
    indents = 0
    is_indenting = True
    with open('zigzag.txt', 'w', encoding='utf-8') as file_obj:
        for i in range(line_limit):
            file_obj.write(" " * indents + "*"*asterisks+ "\n")
            if is_indenting:
                indents += 1
                if indents == indent_limit:
                    is_indenting = not is_indenting
            else:
                indents -= 1
                if indents == 0:
                    is_indenting = not is_indenting

write_zigzag(8, 8, 1000)