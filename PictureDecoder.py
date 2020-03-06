import random
from PIL import Image, ImageDraw

image = Image.open("ans.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
f = open('Decodetext.txt', 'w')
mesage = {}
mesagelen = 0
for i in range (0, 9):
    mesagelen += (pix[0, i // 3][i % 3] % 10) * 10**(8 - i)

print(mesagelen)
letterindex = 0
for i in range(width):
    for j in range(height):
        if(j % 2 == i % 2  and letterindex < mesagelen - 1 and not(i == 0 and (j == 0 or j == 1 or j == 2)) ):
            letterindex += 1
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            letter = chr(r % 10 * 100 + (g % 10) * 10 + b % 10)
            f.write(letter)
f.close()