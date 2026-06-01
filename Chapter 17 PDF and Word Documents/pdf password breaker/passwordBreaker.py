#Chapter 17 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter17.html

import pypdf

dictionary = 'dictionary.txt'
file_name = "Recursion_Chapter1_encrypted.pdf"

with open(dictionary, encoding="UTF-8") as file_obj:
    words = [line.strip() for line in file_obj]

for word in words:
    for attempt in (word.lower(), word.upper()):
        
        reader = pypdf.PdfReader(file_name)

        result = reader.decrypt(attempt)
        print(attempt)
        if result:
            print(f'\nPassword found: {attempt}')
            writer = pypdf.PdfWriter(clone_from=reader)
            output_file = file_name.replace("_encrypted.pdf", "_decrypted.pdf")

            with open(output_file, "wb") as f:
                writer.write(f)
            exit()