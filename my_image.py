from __future__ import print_function
from PIL import Image
im = Image.open('me.jpg')   # me.jpg is foto file in current directory
print(im.format, im.size, im.mode)

im.show()
