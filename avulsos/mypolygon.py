import turtle
import math

bob = turtle.Turtle()


def polyline(t, n, length, angle):
    """Desenha n segmentos de linha com o comprimento e o ângulo (em graus) entre eles.\
    t é uma tartaruga.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)


def circle(t, r):
    arc(t, r, 360)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


# circle(bob, 40)
arc(bob, 50, 30)

turtle.mainloop()
