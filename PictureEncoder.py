import random
from PIL import Image, ImageDraw

def encodePixel(i, j, letter):
    r = pix[i, j][0]
    g = pix[i, j][1]
    b = pix[i, j][2]
    bletter = letter % 10
    gletter = (letter % 100) // 10
    rletter = letter // 100
    r = r - r % 10 + rletter
    if r > 255: r = r - 10
    g = g - g % 10 + gletter
    if g > 255: g = g - 10
    b = b - b % 10 + bletter
    if g > 255: g = g - 10
    return (r, g, b)

image = Image.open("Homer.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
f = open('Text.txt', 'r')
mesage = f.read()
letterindex = 0
for i in range(width):
    for j in range(height):
        point = (pix[i, j][0], pix[i, j][1], pix[i, j][2])
        if i == 0 and j == 0:
            point = encodePixel(i, j, len(mesage)// 1000)
        else:
            if i == 0 and j == 1:
                point = encodePixel(i, j, len(mesage) % 1000)
            else:
                if len(mesage) > letterindex:
                    point = encodePixel(i, j, ord(mesage[letterindex]))
                    letterindex += 1
        draw.point((i, j) , point)
image.save("ans.png", "PNG")
f.close()