#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import os
from pathlib import Path

base = Path.home()

for folder_path, _, files in os.walk(base):
    folder = Path(folder_path)

    for file in files:
        file_path = folder / file

        try:
            size_bytes= file_path.stat().st_size
            #size_bytes = os.path.getsize(file_path)
        except FileNotFoundError:
            continue

        #size_kb = size_bytes / 1024
        size_mb = size_bytes / (1024 ** 2)
        if size_mb > 100:
            print(file_path)
            #print(f"{size_kb:.2f} KB")
            print(f"{size_mb:.2f} MB\n")