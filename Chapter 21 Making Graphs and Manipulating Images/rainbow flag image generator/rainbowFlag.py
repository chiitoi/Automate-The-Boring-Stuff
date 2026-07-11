#Chapter 21 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter21.html

from PIL import Image, ImageDraw

def create_rainbow_flag(width, height):
    im = Image.new('RGBA', (width, height), 'purple')
    draw = ImageDraw.Draw(im)
    y_step = int(height / 6)
    
    draw.rectangle((0, y_step*0, width-1, y_step), fill='red', outline='red')
    draw.rectangle((0, y_step, width-1, y_step*2), fill='orange', outline='orange')
    draw.rectangle((0, y_step*2, width-1, y_step*3), fill='yellow', outline='yellow')
    draw.rectangle((0, y_step*3, width-1, y_step*4), fill='green', outline='green')
    draw.rectangle((0, y_step*4, width-1, y_step*5), fill='blue', outline='blue')
    return im

im = create_rainbow_flag(640, 480)
im.show()

im = create_rainbow_flag(1920, 1080)
im.show()