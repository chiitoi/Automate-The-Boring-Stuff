#Chapter 11 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter11.html

import zipfile

def extract_in_folder(zip_filename, folder):
    with zipfile.ZipFile(f'{zip_filename}.zip') as target_zip:
        file_path = f'{zip_filename}/{folder}/'
        for file in target_zip.namelist():
            #file path looks like: eggs/spam/
            if file.startswith(file_path) :
                target_zip.extract(file, '.')


extract_in_folder('eggs', 'spam')

