#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import os
from pathlib import Path

def find_dup_filenames(folder):
    file_list = {}
    for folder_name, _, file_names in os.walk(folder):
        for file in file_names:
            #set a key for each filename and initialize it with an empty list
            file_list.setdefault(file, [])
            file_list[file].append(folder_name)

    keys_with_one_value = []
    for key, value in file_list.items():
        #filtering out all the items that only have one unique file
        if len(value) < 2:
            keys_with_one_value.append(key)
    
    for key in keys_with_one_value:
        del file_list[key]
    
    return file_list

def print_duplicate_files(file_list):
    #prints the list of duplicate filenames to the terminal and saves a .txt file with all the duplicate files
    #WARNING: This does not check file contents, the same filename may contain different data
    with open("duplicate.txt", 'w') as file_obj:
        for key, values in file_list.items():
            file_obj.write(f'{key}\n')
            print(key)
            for path in values:
                file_path = Path(path) / key
                print(f'    {file_path}')
                file_obj.write(f'    {file_path}\n')
            
#change to Path.home() to scan your own home directory
#WARNING: Using Path.home() can result in a large text file
base_folder = Path.cwd()

duplicates = find_dup_filenames(base_folder)
print_duplicate_files(duplicates)