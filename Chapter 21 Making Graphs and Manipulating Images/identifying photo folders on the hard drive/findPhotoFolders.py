#Chapter 21 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter21.html

# Import modules and write comments to describe this program.
import os
from PIL import Image

for folder_name, subfolders, filenames in os.walk('C:\\'):
    num_photo_files = 0
    num_non_photo_files = 0
    for filename in filenames:
        # Check if the file extension isn't .png or .jpg.
        #print(folder_name)
        #print(filename)
        if not filename.lower().endswith(('.png', '.jpg')):
            num_non_photo_files += 1
            continue  # Skip to the next filename.

        # Open image file using Pillow.
        filepath = os.path.join(folder_name, filename)
        
        try:
            with Image.open(filepath) as im_file:
                # Check if the width & height are larger than 500.
                if im_file.width > 500 and im_file.height > 500:
                    # Image is large enough to be considered a photo.
                    num_photo_files += 1
                else:
                    # Image is too small to be a photo.
                    num_non_photo_files += 1
        except Exception:
            # If the file fails to open then consider it a non-photo
            num_non_photo_files += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if num_photo_files > num_non_photo_files:
        print(folder_name)