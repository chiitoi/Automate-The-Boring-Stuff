#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import shutil, os
from pathlib import Path

def selective_copy(old_folder, new_folder, file_type):
    #get the folder path to the current working directory
    base = Path.cwd()

    #create paths with the source folder and the destination folder
    src_base = base / old_folder
    dest_base = base / new_folder

    #create the destination folder
    dest_base.mkdir(parents=True, exist_ok=True)

    copied_list = []
    print(f'\nCopying "{file_type}" files from: \n{src_base}')
    print(f'\nTo:\n{dest_base}\n')

    for folder_name, _, filenames in os.walk(src_base):
        #creating a new path inside the source folder for refernece
        folder_path = Path(folder_name)
        for file in filenames:
            #file path of each file within the source folder
            src_file = folder_path / file      

            #check if the extension matches what the user wants
            if src_file.suffix == file_type: 
                #creating relative paths if the source folder contains folders
                relative_path = folder_path.relative_to(src_base)

                #if the relative path is the source folder it returns WindowsPath('.') which is the current folder
                #mkdir doesn't run anything meaningful in that scenario
                target_folder = dest_base / relative_path
                target_folder.mkdir(parents=True, exist_ok=True)

                dst_file = target_folder / file

                print(f'Found: {src_file}')
                shutil.copy(src_file, dst_file)
                copied_list.append((src_file, dst_file))

    print(f'\nCopied files to {dest_base}:')
    for src, dst in copied_list:
        print(f'{src}\n->\n{dst}\n')

selective_copy('spam1', 'spam2', '.txt')