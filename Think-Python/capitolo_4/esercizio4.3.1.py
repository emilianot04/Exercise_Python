import turtle
bob = turtle.Turtle()


def quadrato(t):
    for i in range(4):
        bob.fd(100)
        bob.lt(90)

quadrato(bob)
turtle.mainloop()