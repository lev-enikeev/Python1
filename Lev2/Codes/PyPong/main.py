import turtle

T = turtle.Pen()
#T = turtle.pen(fillcolor="black", pencolor="red", pensize=10)
T.st()
T.speed(10000)
for i in range(1000):
    T.fd(i)
    T.left(91)