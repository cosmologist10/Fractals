#!/usr/bin/python

from PIL import Image, ImageDraw


def sierpinski(values, steps, update_image, x):
        update_image.line((values[0], values[1]))
        update_image.line((values[1], values[2]))
        update_image.line((values[0], values[2]))

        x1 = (values[0][0] + values[1][0]) / 2
        y1 = (values[0][1] + values[1][1]) / 2

        x2 = (values[1][0] + values[2][0]) / 2
        y2 = (values[1][1] + values[2][1]) / 2

        x3 = (values[2][0] + values[0][0]) / 2
        y3 = (values[2][1] + values[0][1]) / 2

        values2 = ((x1, y1), (x2, y2), (x3, y3))

        x += 1
        if x <= steps:
            sierpinski((values[0], values2[0], values2[2]), steps, update_image, x)
            sierpinski((values[1], values2[0], values2[1]), steps, update_image, x)
            sierpinski((values[2], values2[1], values2[2]), steps, update_image, x)


def draw(image):
    return ImageDraw.Draw(image)

steps = 10

values = ((0, 500), (500, 500), (250, 0))

size = values[1]
picture = Image.new('1', size, color="white")
update_image = draw(picture)

sierpinski(values, steps, update_image, 0)

imagename = "gasket.png"
picture.save(imagename)
