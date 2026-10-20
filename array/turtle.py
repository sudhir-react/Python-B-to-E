from turtle import *
from math import *
from colorsys import *

# Setup turtle canvas
tracer(0)
bgcolor("black")
up()

# Draw phyllotaxis spiral pattern
for i in range(2500):
    a = i *1375 * pi /180
    r =9 * sqrt(i)
    goto(r*cos(a), r*sin(a))
    c = hsv_to_rgb(i/2500, 1, 1)
    color(c)
    dot(2 + i/150)
update()
done()