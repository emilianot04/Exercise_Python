#Per esercitarvi, scrivete una funzione di nome compara che prenda due valori, x e y, e restituisca 1 se x > y,0 se x == y,e -1 se x < y.
def compara(x,y):
    if (x>y):
        print(1)
    elif(x==y):
        print(0)
    elif(x<y):
        print(-1)


compara(12,12)

#Come esercizio, usate lo sviluppo incrementale per scrivere una funzione di nome ipotenusa, che restituisca la lunghezza dell’ipotenusa di un triangolo rettangolo, date le lunghezze dei cateti come argomenti.

import math
def ipotenusa (cateto1,cateto2):
    somma = (cateto1*cateto1) + (cateto2*cateto2)
    risultato = math.sqrt(somma)
    print(risultato)

ipotenusa(13.3,15.6)


#Scrivete ora, per esercizio, una funzione compreso_tra(x, y, z) che restituisca True se x ≤ y ≤ z o False altrimenti.

def compreso_tra(x,y,z):
    if (x<= y <= z):
        print ('true')
    else:
        print ('false')
    
compreso_tra(1,2,3)


#fattoriale

def fattoriale(n):
    if n == 0:
        return 1
    else:
        ricors = fattoriale(n-1)
        risultato = n * ricors
        return risultato

print(fattoriale(3))


def stampa(): 
    print('Ciao') 
 
stampa()


