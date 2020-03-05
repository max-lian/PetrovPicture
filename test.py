from PIL import Image, ImageDraw

image = Image.open("ans.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
for i in range(width):
    for j in range(height):
        print(pix[i, j]),
    print ('\n')