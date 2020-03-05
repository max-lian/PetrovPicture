import random
from PIL import Image, ImageDraw
pix = {}
def encoding():
    global pix
    image = Image.open("port.png")
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    print(width, height)

    pix = image.load()
    f = open('test1million.txt', 'r')
    mesage = f.read()
    print(len(mesage))
    image.save("ans.png", "PNG")
    #interval = (width * height) // (len(mesage) ** 2)
    f.close()
    letterindex = 0
    for i in range(width):
        for j in range(height):
            point = (pix[i, j][0], pix[i, j][1], pix[i, j][2])
            if i == 0:
                if j == 0:
                    point = encodePixel(i, j, len(mesage) // 1000000)
                if j == 1:
                    point = encodePixel(i, j, len(mesage) % 1000000 // 1000)
                if j == 2:
                    point = encodePixel(i, j, len(mesage) % 1000)
            if j % 2 == i % 2 and len(mesage) > letterindex and not (i == 0 and (j == 0 or j == 1 or j == 2)):
                point = encodePixel(i, j, ord(mesage[letterindex]))
                letterindex += 1
            draw.point((i, j), point)
    image.save("ans.png", "PNG")
    f.close()
def encodePixel(i, j, letter):
    #print(chr(letter))
    r = pix[i, j][0]
    g = pix[i, j][1]
    b = pix[i, j][2]
    bletter = letter % 10
    gletter = (letter % 100) // 10
    rletter = letter // 100
    r = calcpixel(r, rletter)
    g = calcpixel(g, gletter)
    b = calcpixel(b, bletter)
    return (r, g, b)

def calcpixel(color, colorletter):
    tempcolor = color - (color % 10 - colorletter)
    if (color % 10 - colorletter > 5):
        tempcolor = tempcolor + 10
    if color % 10 - colorletter < -5:
        tempcolor = tempcolor - 10
    color = tempcolor
    if color > 255: color = color - 10
    if color < 0: color = color + 10
    return color

if __name__ == "__main__":
    encoding()
