#!/usr/bin/python

# Import Image and ImageDraw for creating new images and retouching existing images
from PIL import Image, ImageDraw


def fractal(steps):
    def sierpinski_display(values):
        update_image.line((values[0], values[1]))
        update_image.line((values[1], values[2]))
        update_image.line((values[0], values[2]))

    def sierpinski_compute(values):
        x1 = (values[0][0] + values[1][0]) / 2
        y1 = (values[0][1] + values[1][1]) / 2

        x2 = (values[1][0] + values[2][0]) / 2
        y2 = (values[1][1] + values[2][1]) / 2

        x3 = (values[2][0] + values[0][0]) / 2
        y3 = (values[2][1] + values[0][1]) / 2

        values2 = [[x1, y1], [x2, y2], [x3, y3]]

        p=[values[0], values2[0], values2[2]]
        q=[values[1], values2[0], values2[1]]
        r=[values[2], values2[1], values2[2]]

    sierpinski_display(values)
    if x<=steps:
        sierpinski_display(p)
        sierpinski_display(q)
        sierpinski_display(r)
        sierpinski_compute(p)
        sierpinski_compute(q)
        sierpinski_compute(r)

    x+=1
def draw(image):
    return ImageDraw.Draw(image)

p=[]
q=[]
r=[]
x = 1
values = [[0, 500], [500, 500], [250, 0]]
size = values[1]
picture = Image.new('1', size, color="white")
update_image = draw(picture)
imagename = "gasket1.png"
picture.save(imagename)

if __name__ == "__main_":
    fractal(10)
