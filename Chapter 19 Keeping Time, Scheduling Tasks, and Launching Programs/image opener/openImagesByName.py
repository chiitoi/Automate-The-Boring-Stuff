#Chapter 19 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter19.html

import os
from pathlib import Path

def open_images_by_name(image_folder, name_match):
    folder = Path(image_folder)
    if not folder.exists():
        raise FileNotFoundError(f'Cannot find folder "{image_folder}"')
    
    formats = ('.jpg', '.png', '.webp')
    name_match = name_match.lower()

    for file in folder.iterdir():
        extension = file.suffix.lower()

        #check if the file is really a file
        #also check for case insensitive name and extension
        if file.is_file() and name_match in file.name.lower() and extension in formats:
            os.startfile(file)

folder_name = 'images'
search_term = 'cat'

open_images_by_name(folder_name, search_term)