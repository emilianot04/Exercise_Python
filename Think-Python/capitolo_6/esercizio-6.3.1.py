#palindromo

def prima(parola):
    return parola[0]

def ultima(parola):
    return parola[-1]

def mezzo(parola):
    return parola[1:-1]

mezzo('c')

#1 - scrivete queste funzioni in un file script palindromo.py e provatele. Cosa succede se chiamate mezzo con una stringa di due lettere? E di una lettera? E con la stringa vuota, che si scrive '' e non contiene caratteri?
# due lettere  = nulla
# una = nulla
# '' = nulla

# 2 Scrivete una funzione di nome palindromo che riceva una stringa come argomento e restituisca True se è un palindromo e False altrimenti. Ricordate che potete usare la funzione predefinita len per controllare la lunghezza di una stringa.

def palindroma(parola):
    if  len(parola) <= 1:
        return True
    if prima(parola) != ultima(parola):
        return False
    return palindroma(mezzo(parola))

print(palindroma('ciao'))
print(palindroma('otto'))
