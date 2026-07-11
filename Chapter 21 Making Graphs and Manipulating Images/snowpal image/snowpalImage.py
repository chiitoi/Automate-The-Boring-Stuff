#Chapter 21 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter21.html

from PIL import Image, ImageDraw

#intialize the image with a skyblue background
im = Image.new('RGBA', (1000, 1000), 'skyblue')
draw = ImageDraw.Draw(im)

#create snow on the ground
draw.rectangle((0, 600, 1000, 1000), fill='white')

#draw 3 circles for the body
draw.ellipse((300, 575, 700, 975), fill='white', outline='black', width=3)
draw.ellipse((350, 300, 650, 600), fill='white', outline='black', width=3)
draw.ellipse((400, 125, 600, 325), fill='white', outline='black', width=3)

#draw 2 rectangles for the top hat
draw.rectangle((410, 125, 590, 145), fill='black', outline='black')
draw.rectangle((440, 25, 560, 145), fill='black', outline='black')

#draw 2 lines for the arms
draw.line((600, 400, 700, 325), fill='brown', width=7)
draw.line((410, 425, 300, 300), fill='brown', width=7)

im.show()