''' Используя библиотеку Pillow, создать какой-либо фильтр,
который каким-либо образом изменяет цвета пикселов на готовом изображении.'''

from PIL import Image, ImageOps

INPUT_PATH = 'pacman.png'
OUTPUT_PATH = 'neg_pacman.png'

original_image = Image.open(INPUT_PATH)

negative_image = ImageOps.invert(original_image)

negative_image.save(OUTPUT_PATH)
