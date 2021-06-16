#importo modulo math
import math

#creo una funzione
def stampa_brani():
    print('prima riga')
    print('seconda riga')

stampa_brani()


# richiamo una funzione in una funzione
def ripeti_brani():
    stampa_brani()
    stampa_brani()
    stampa_brani()

ripeti_brani()

#se sposto la chimata dui funzione ripeti_brani() in alto 
#errore NameError: name 'ripeti_brani' is not defined

# funzioni con parametri

def stampa_con_parametro(par):
    print(par)
    print(par*4)

stampa_con_parametro('ciao ')
stampa_con_parametro(math.pi)

#3.8 Variabile e paramentri sono locali

def cat2volte(parte1,parte2):
    cat = parte1 + parte2
    stampa_con_parametro(cat) #richiamo la funzione  stampa_con_parametro

cat2volte('ciao', 'mondo')