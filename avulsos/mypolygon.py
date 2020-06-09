import turtle
bob = turtle.Turtle()

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
#rrr
polygon(bob, 10, 10)
