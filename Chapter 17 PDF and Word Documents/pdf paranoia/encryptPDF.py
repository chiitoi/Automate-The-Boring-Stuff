#Chapter 17 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter17.html

import pypdf, os, sys
from pathlib import Path

if len(sys.argv) != 2:
    print(f'Please input a password to encrypt the PDF files.')
    sys.exit()

password = sys.argv[1]

base_folder = Path.cwd()
for folder_name, _, filenames in os.walk(base_folder):
    for filename in filenames:
        if filename.lower().endswith('.pdf') and not '_encrypted' in filename.lower():
            filepath = Path(folder_name) / filename
            output_path = filepath.parent / f"{filepath.stem}_encrypted.pdf"
            #print(f'original pdf filepath:\n\t{filepath}')
            #print(f'new filepath:\n\t{output_path}')
            try:
                writer = pypdf.PdfWriter()
                writer.append(str(filepath))
                writer.encrypt(password, algorithm='AES-256')
                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)
                print(f'Encrypted {filename} as\n\t{output_path}')

                #check and decrypt the file to see if it was encrypted correctly
                reader = pypdf.PdfReader(output_path)
                if reader.is_encrypted and reader.decrypt(password).name != 'NOT_DECRYPTED':
                    print(f'\t"{Path(output_path).name}" is properly encrypted.\n')
                else:
                    print(f'Something went wrong, encryption has failed.')
            except Exception as e:
                print(f'Failed: {filepath}')
                print(f'Error: {e}')
"""
print()

for folder_name, _, filenames in os.walk(base_folder):
    for filename in filenames:
        if '_encrypted' in filename.lower():
            filepath = Path(folder_name) / filename
            reader = pypdf.PdfReader(filepath)
            if reader.is_encrypted and reader.decrypt(password).name != 'NOT_DECRYPTED':
                print(f'{filename} is properly encrypted.')
"""