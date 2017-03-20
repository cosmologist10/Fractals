#!/usr/bin/python

"""

Add a module doc string to explain what the modules does

"""

from PIL import Image, ImageDraw


def sierpinski(values, steps, update_image, x):

        # This is presentation, as in the following
        # 3 lines of code updates a structure which
        # produces the display output.
        update_image.line((values[0], values[1]))
        update_image.line((values[1], values[2]))
        update_image.line((values[0], values[2]))

        # This is computation. The next 7-8 lines
        # computes the co-ordinates of the next triangle
        
        x1 = (values[0][0] + values[1][0]) / 2
        y1 = (values[0][1] + values[1][1]) / 2

        x2 = (values[1][0] + values[2][0]) / 2
        y2 = (values[1][1] + values[2][1]) / 2

        x3 = (values[2][0] + values[0][0]) / 2
        y3 = (values[2][1] + values[0][1]) / 2

        values2 = ((x1, y1), (x2, y2), (x3, y3))

        # This is the continuation part. The following lines
        # takes the code to the next step and repeats the process.
        x += 1
        if x <= steps:
            sierpinski((values[0], values2[0], values2[2]), steps, update_image, x)
            sierpinski((values[1], values2[0], values2[1]), steps, update_image, x)
            sierpinski((values[2], values2[1], values2[2]), steps, update_image, x)

        # Problems
        # 1. Mixing presentation code with computation code.
        # 2. Using 3 way recursion which can be simplified into iteration
        #    3 way recursion means at every call your stack is split into
        #    3 child stacks, so after a while the memory will get exhausted!
        #    Also this is very inefficient way of coding,
        # 3. Never use recursion more than 2 way.

        # Fixes
        # 1. Split your code into two functions, one which does computation
        # of triangle co-ordinates and puts them into a list.
        # 2. The list can iterate "steps" times. Each time a sub-triangle is
        # calculated and co-ordinates appended to the list.
        # 3. The first function returns this list.

        # 4. The second function accepts this list and the update_image as arguments,
        # iterates through it and adds lines for each triangle and also saves the
        # contents to a filename.


def draw(image):
    return ImageDraw.Draw(image)

# These should be under an if __name__ == "__main__" section.
# if __name__ == "__main__":
# 
# ... do the following below.

# These should be moved to the new computation function.
steps = 10
values = ((0, 500), (500, 500), (250, 0))

size = values[1]

# These should be moved to the new presentation function.
picture = Image.new('1', size, color="white")
update_image = draw(picture)

# This one function call will be replaced with two
# calls - one to the computation one and next to the
# presentation one.
sierpinski(values, steps, update_image, 0)

# This will be moved to the new presentation function.
imagename = "gasket.png"
picture.save(imagename)

# Suggested function names.
# 1. Computation - sierpinski_compute
# 2. Presentation - sierpinski_display
