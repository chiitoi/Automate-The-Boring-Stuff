#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import shutil, os, re
from pathlib import Path
#regex that captures the prefix, the month, day, year, and the suffix
#works with all files in the subfolder of where the current directory is
american_style_regex = re.compile(r'(.*?)(\d{2})-(\d{2})-(\d{4})(.*)')

def convert_date():
    base_folder = Path.cwd()

    for folder_name, _, filenames in os.walk(base_folder):
        for file in filenames:
            result = american_style_regex.search(file)
            if result:
                base_source = Path(folder_name)
                file_path = base_source / file

                prefix, month, day, year, suffix = result.groups()
                new_file = f"{prefix}{day}-{month}-{year}{suffix}"
                new_file_path = base_source / new_file

                print(f"Renaming {file} -> {new_file}")

                #if the new file doesn't exist then we rename the old file to the new one
                #otherwise it prints to the terminal that the existing file already exists
                if not new_file_path.exists():
                    shutil.move(file_path, new_file_path)
                else:
                   print(f"Skipped (already exists): {new_file}")

convert_date()