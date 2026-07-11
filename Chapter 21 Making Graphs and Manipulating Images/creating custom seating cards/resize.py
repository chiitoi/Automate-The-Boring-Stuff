from PIL import Image

watermark = Image.open('flower.png')
width, height = watermark.size
quarter_size = watermark.resize((int(width / 4), int(height / 4)))
quarter_size('flower_resized.png')
