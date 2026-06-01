#Chapter 17 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter17.html

import pypdf, os, sys
from pathlib import Path

if len(sys.argv) != 2:
    print(f'Please input a password to decrypt the PDF files.')
    sys.exit()

password = sys.argv[1]

base_folder = Path.cwd()

for folder_name, _, filenames in os.walk(base_folder):
    for filename in filenames:
        if filename.lower().endswith('_encrypted.pdf'):
            filepath = Path(folder_name) / filename
            output_path = filepath.parent / filename.replace("_encrypted.pdf", "_decrypted.pdf")

            #print(output_path)
            try:
                reader = pypdf.PdfReader(filepath)
                result = reader.decrypt(password)

                #check if the password worked, if not skip the file
                if not result:
                    print(f'Incorrect password for {filename}')
                    continue
                
                writer = pypdf.PdfWriter()

                for page in reader.pages:
                    writer.add_page(page)

                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                print(f'Decrypted {filename} as\n\t{output_path}')

            except Exception as e:
                print(f'Failed: {filepath}')
                print(f'Error: {e}')