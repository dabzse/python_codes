import turtle


t = turtle
T = turtle.Turtle()
TS = turtle.Screen()

TS.bgcolor("black")
T.pensize(1)
T.speed(13)


for _ in range(6):
    for colors in ["red", "cornflower blue", "lime", "spring green", "light blue", "blue"]:
        T.color(colors)
        T.circle(160)
        T.left(10)
        T.hideturtle()
t.done()


## tested on Fedora 35 with python3.11.0.a6
## you can change range(6) to range(60), but then should change T.left(10) to T.left(1)
## change the T.circle # it's a size of a circle
## change some colors #! note that in this case you should have 6 colors
## and also the speed, pensize, bgcolor
