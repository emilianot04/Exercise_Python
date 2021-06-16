import turtle
bob = turtle.Turtle()


def quadrato(t, lunghezza):
    for i in range(4):

        bob.fd(lunghezza)
        bob.lt(90)
        
quadrato(bob, 100)
