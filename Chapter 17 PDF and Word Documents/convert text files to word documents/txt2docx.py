#Chapter 17 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter17.html

import docx, os

def str_to_docx(text, word_filename):
    doc = docx.Document()
    for line in text.splitlines():
        doc.add_paragraph(line)
    doc.save(word_filename)
    print(f'Saved file as {word_filename}')

txt_file = 'bacon.txt'

for file in os.listdir('.'):
    if file.endswith('.txt'):
        with open(file, encoding="UTF-8") as file_obj:
            print(f'Converting {file}...')
            #get the text contents of the file
            text_file = file_obj.read()
            
            #convert to docx
            str_to_docx(text_file, file + '.docx')