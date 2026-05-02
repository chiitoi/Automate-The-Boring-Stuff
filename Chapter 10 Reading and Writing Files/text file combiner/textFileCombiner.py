#Chapter 10 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter10.html

def combine_two_text_files(file_one, file_two, output_name):
    with open(output_name, 'w', encoding="UTF-8") as out_file_obj:
        with open(file_one, encoding="UTF-8") as in_file_obj:
            out_file_obj.write(in_file_obj.read())
        
        with open(file_two, encoding="UTF-8") as in_file_obj:
            out_file_obj.write(in_file_obj.read())

combine_two_text_files('spam.txt', 'eggs.txt', 'output.txt')

