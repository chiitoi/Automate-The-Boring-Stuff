#Chapter 21 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter21.html

from PIL import Image, ImageOps
import random

#creates a mirrored tile pattern:
#center tiles are inverted
#left side uses alternating transformations
#right side mirrors the left side
def make_tile(image_name, horizontal_length, vertical_length):
    base_im = Image.open(image_name)
    width, height = base_im.size
    #create a blank image in the size of the horizontal and vertical lengths
    tiled_im = Image.new('RGBA', (int(width*horizontal_length), int(height*vertical_length)))

    #determine the center columns:
    #odd widths have one center tile, even widths have two center tiles
    if horizontal_length % 2:
        center_indices = {horizontal_length // 2}
    else:
        center_indices = {
            horizontal_length // 2 - 1,
            horizontal_length // 2,
    }

    middle = horizontal_length // 2

    for index, left in enumerate(range(0, tiled_im.width, width)):
        for top in range(0, tiled_im.height, height):
            #work on a copy so that the original image isn't modified
            copy_im = base_im.copy()

            #apply special treatment to the center tiles
            if index in center_indices:
                copy_im = ImageOps.invert(copy_im)
            
            #left half: create a pattern that the right half wil mirror
            if index < middle:
                if index == 0:
                    pass  # original
                elif index % 2 == 1:
                    choice = random.randint(0, 1)
                    if choice == 0:
                        copy_im = copy_im.rotate(180)
                    else:
                        copy_im = copy_im.transpose(Image.FLIP_TOP_BOTTOM)
                else:
                    pass

            #right half: outermost tile becomes a horizontal flip
            else:
                #find the matching tile on the left side
                mirrored_left = horizontal_length - 1 - index
                if mirrored_left == 0:
                    copy_im = copy_im.transpose(Image.FLIP_LEFT_RIGHT)
                elif mirrored_left % 2 == 1:
                    choice = random.randint(0, 1)
                    if choice == 0:
                        copy_im = copy_im.rotate(180)
                    else:
                        copy_im = copy_im.transpose(Image.FLIP_TOP_BOTTOM)
                else:
                    copy_im = copy_im.transpose(Image.FLIP_LEFT_RIGHT)

            #place the transformed tile into the final image
            tiled_im.paste(copy_im, (left, top))

    name = f'tiled{horizontal_length}.png'
    tiled_im.save(name)

file_name = 'zophie.png'
make_tile(file_name, 15, 10)