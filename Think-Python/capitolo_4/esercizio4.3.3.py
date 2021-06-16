import turtle
bob = turtle.Turtle()


def poligono(t, lunghezza, n):
    lati = (360/n)
    for i in range(n):
        bob.fd(lunghezza)
        bob.lt(lati)
        


poligono(bob, 150, 7)
turtle.mainloop()