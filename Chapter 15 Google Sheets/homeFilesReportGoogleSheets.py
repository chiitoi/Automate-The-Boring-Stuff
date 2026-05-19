#Chapter 15 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter15.html

import ezsheets, os
from pathlib import Path
import pprint

def get_home_folder_size():
    filenames_and_sizes = []

    # Loop over everything in the home folder:
    for filename in os.listdir(Path.home()):
        absolute_file_path = Path.home() / filename

        # Skip folders/directories:
        if absolute_file_path.is_dir():
            continue

        # Get file size:
        try:
            file_size = absolute_file_path.stat().st_size
        except Exception:
            # Skip files with permissions errors:
            continue

        # Record filename and size:
        filenames_and_sizes.append((filename, file_size))

    return filenames_and_sizes

# Uncomment to print the hundred largest filenames and sizes:
#pprint.pprint(get_home_folder_size())


def make_google_sheets_report(filenames_and_sizes):
    #pprint.pprint(filenames_and_sizes)
    ss = ezsheets.Spreadsheet()
    ss.title = 'Home Files Report'
    sheet = ss.sheets[0]
    file_name = ['Filename']
    size = ['Bytes']

    #create the lists first without having the make multiple api calls
    for item in filenames_and_sizes:
        file_name.append(item[0])
        size.append(item[1])

    #add the lists in two api calls
    sheet.updateColumn(1, file_name)
    sheet.updateColumn(2, size)

make_google_sheets_report(get_home_folder_size())