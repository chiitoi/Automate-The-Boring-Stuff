#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import shutil, os
from pathlib import Path

def renumber(prefix, suffix, number):
    src_base = Path.cwd()
    file_list = []

    for folder_name, _, filenames in os.walk(src_base):
        folder = Path(folder_name)

        for file in filenames:
            if file.startswith(prefix) and file.endswith(suffix):
                #remove the prefix and suffix so we are only left with the number
                #spam001.txt -> 001 -> 1 after int conversion
                num = int(file.replace(prefix, "").replace(suffix, ""))
                file_list.append((num, folder / file))

    #if we don't sort then we will overwrite files when moving forward
    file_list.sort

    for num, file_path in reversed(file_list):
        #for any file that is above the index, it will rename them and add a gap inbetween
        #does not check if there already is a gap so it will keep adding more gaps every time the program is run
        if num >= number:
            new_num = num + 1
            new_name = f"{prefix}{new_num:03}{suffix}"
            new_path = file_path.with_name(new_name)

            print(f"Renaming {file_path.name} -> {new_name}")
            shutil.move(file_path, new_path)

renumber('spam', '.txt', 3)