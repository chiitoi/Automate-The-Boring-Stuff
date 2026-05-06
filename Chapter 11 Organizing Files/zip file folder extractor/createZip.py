#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import zipfile, os
from pathlib import Path
folder = "eggs"
base_source = Path(folder)

with zipfile.ZipFile(f'{folder}.zip', 'w') as example_zip:
    for folder_name, subfolder, file_list in os.walk(base_source):
        folder_name = Path(folder_name)
        for file in file_list:
            print(folder_name / file)
            example_zip.write(folder_name / file, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)