from turtle import *
from math import *

iter = 9000
disk_ratio = 0.5
factor = 0.5 + sqrt(1.25)
screen = getscreen()

(win_width, win_height) = screen.screensize()

y = 0.0
x = 0.0

max_rad = pow(iter, factor) / iter

bgcolor("light blue")
hideturtle()
tracer(0,0)
for i in range(iter + 1):
    r = pow(i, factor) / iter
    if r / max_rad < disk_ratio:
        pencolor("black")
    else:
        pencolor("yellow")
    
    theta = 2 * pi * factor * i
    up()
    setposition(x + r * sin(theta), y + r * cos(theta))
    down()
    circle(10.0 * i / (1.0 * iter))

update()
done()