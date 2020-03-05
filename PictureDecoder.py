import random
from PIL import Image, ImageDraw

image = Image.open("ans.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
f = open('Decodetext.txt', 'w')
mesage = {}
mesagelen = pix[0, 0][0] % 10 * 100000000 + pix[0, 0][1] % 10 * 10000000 + pix[0, 0][2] % 10 * 1000000 \
            + pix[0, 1][0] % 10 * 100000 + pix[0, 1][1] % 10 * 10000 + pix[0, 1][2] % 10 * 1000 \
            + pix[0, 2][0] % 10 * 100 + pix[0, 2][1] % 10 * 10 + pix[0, 2][2] % 10
for i in range(width):
    for j in range(height):
        if(i * height + j <= mesagelen + 1 and not(i == 0 and (j == 0 or j == 1 or j == 2)) ):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            letter = chr(r % 10 * 100 + (g % 10) * 10 + b % 10)
            f.write(letter)
f.close()