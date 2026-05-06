#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import shutil, os
from pathlib import Path

def renumber(prefix, suffix):
    src_base = Path.cwd()
    file_list = []
    for folder_name, _, filenames in os.walk(src_base):
        folder = Path(folder_name)
        for file in filenames:
            #only finds files that have the exact prefix and suffix
            #spam006.sh is ignored because it doesn't match .txt
            if file.startswith(prefix) and file.endswith(suffix):
               file_list.append(folder / file)

    file_list.sort()

    for index, file in enumerate(file_list, start=1):
        new_name = f"{prefix}{index:03}{suffix}"
        new_path = file.with_name(new_name)
        if file.name != new_name:
            print(f'Renaming {file.name} -> {new_name}')
            shutil.move(file, new_path)

renumber('spam', '.txt')
