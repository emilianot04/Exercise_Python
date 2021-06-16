import turtle
import math
bob = turtle.Turtle()

def poligono(t, lunghezza, n):
    lati = 360/n
    for i in range(n):
        t.fd(lunghezza)
        t.lt(lati)     

poligono(bob,7,70)

def cerchio(t,r):
    circoferenza= 2 * math.pi * r
    n = 50
    lunghezza = circoferenza / n
    poligono(t,n,lunghezza)   
          
cerchio(bob,100)
turtle.mainloop()