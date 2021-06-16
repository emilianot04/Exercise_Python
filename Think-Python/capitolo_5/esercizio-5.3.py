# Esercizio 5.3.1

def triangolo(a, b, c):
    if a > (b+c) or b > (a+c) or c > (a+b):
        print('non si può formare')
    else:
        print('si può formare')


  # triangolo(1, 2, 4)

# Esercizio 5.3.2

primo = input ('inserisci valore a\n')
secondo = input ('inserisci valore b\n')
terzo = input ('inserisci valore c\n')


triangolo(primo, secondo, terzo)