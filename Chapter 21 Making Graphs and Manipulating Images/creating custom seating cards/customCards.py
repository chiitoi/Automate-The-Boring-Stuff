#Chapter 21 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter21.html

import os
from PIL import Image, ImageDraw

os.makedirs('cardInvites', exist_ok=True)
guest_file = 'guests.txt'

logo_im = Image.open('flower_resized.png')
logo_width, logo_height = logo_im.size

#calculates the left pixel from the black border
def calculate_pixels(drawObj, left, right, sentence):
    text_width = drawObj.textlength(sentence, font_size=12)
    return left + ((right - left) - text_width) / 2

with open(guest_file, encoding="UTF-8") as file_obj:
    for line in file_obj:
        name = line.strip()
        card = Image.new('RGBA', (300, 372), 'white')
        draw = ImageDraw.Draw(card)

        #the inner border of the image is 288×360 as per the assignment guidelines
        #draw method is inclusive so we offset by 1 pixel to get to 293 and 365
        border_left = 6
        border_right = 293
        border_top = 6
        border_bottom = 365

        
        draw.rectangle((border_left, border_top, border_right, border_bottom), outline = 'black')
        
        #center the text using calculate_pixels()
        first_line = 'It would be a pleasure to have the company of'
        left_pixel = calculate_pixels(draw, border_left, border_right, first_line)
        draw.text((left_pixel, 25), first_line, font_size=12, fill="black")

        left_pixel = calculate_pixels(draw, border_left, border_right, name)
        draw.text((left_pixel, 55), name, font_size=12, fill='black')

        third_line = 'at 11010 Memory Lane on the Evening of'
        left_pixel = calculate_pixels(draw, border_left, border_right, third_line)
        draw.text((left_pixel, 85), third_line , font_size=12, fill='black')

        date_line = 'April 1st'
        left_pixel = calculate_pixels(draw, border_left, border_right, date_line)
        draw.text((left_pixel, 115), date_line , font_size=12, fill='black')

        fifth_line = "at 7 o'clock"
        left_pixel = calculate_pixels(draw, border_left, border_right, fifth_line)
        draw.text((left_pixel, 145), fifth_line , font_size=12, fill='black')

        #center horizontally inside the border
        logo_x = border_left + ((border_right - border_left - logo_width) // 2)

        #get bottom half of the card
        bottom_half_top = card.height // 2

        #center vertically inside the bottom half
        logo_y = bottom_half_top + ((border_bottom - bottom_half_top - logo_height) // 2)

        card.paste(logo_im, (logo_x, logo_y), logo_im)

        file_name = f'{name}.png'
        card.save(os.path.join('cardInvites', file_name))