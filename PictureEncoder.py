import random
from PIL import Image, ImageDraw

def encodePixel(i, j, letter):
    r = pix[i, j][0]
    g = pix[i, j][1]
    b = pix[i, j][2]
    bletter = letter % 10
    gletter = (letter % 100) // 10
    rletter = letter // 100
    r = r - (r % 10 - rletter)
    if (r % 10 - rletter > 5):
        r = r + 10
    if r % 10 - rletter < -5:
        r = r - 10
    if r > 255: r = r - 10
    if r < 0: r = r + 10
    g = g - g % 10 + gletter
    if (g % 10 - gletter > 5):
        g = g + 10
    if g % 10 - gletter < -5:
        g = g - 10
    if g > 255: g = g - 10
    if g < 0: g = g + 10
    b = b - b % 10 + bletter
    if (b % 10 - bletter > 5):
        b = b + 10
    if b % 10 - bletter < -5:
        b = b - 10
    if b > 255: b = b - 10
    if b < 0: b = b + 10
    return (r, g, b)

image = Image.open("port.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
print(width, height)
pix = image.load()
f = open('Test.txt', 'r')
mesage = f.read()
letterindex = 0
for i in range(width):
    for j in range(height):
        point = (pix[i, j][0], pix[i, j][1], pix[i, j][2])
        if i == 0:
            if j == 0:
                point = encodePixel(i, j, len(mesage)// 1000000)
            if j == 1:
                point = encodePixel(i, j, len(mesage) % 1000000 // 1000)
            if j == 2:
                point = encodePixel(i, j, len(mesage) % 1000)
        if len(mesage) > letterindex and not(i == 0 and (j == 0 or j == 1 or j == 2)):
            point = encodePixel(i, j, ord(mesage[letterindex]))
            letterindex += 1
        draw.point((i, j) , point)
image.save("ans.png", "PNG")
f.close()