#len
frutto = 'banana'
print(len(frutto))


#Attraversamento utilizzando ciclo While
indice = 0
while indice < len(frutto):
    lettera = frutto[indice]
    print(lettera)
    indice = indice + 1



#anatroccoli
prefissi = 'JKLMNOPQ'
suffisso = 'ack'
for lettera in prefissi:
    if(lettera == 'O' or lettera == 'Q'):
        print(lettera + 'u' + suffisso)
    else:
        print(lettera + suffisso)

#slice
s = 'Monty Python'
s[0:5] 
s[6:12]
print(s[0:5])
print(s[6:12])
print(s[6:6])



#cambio lettera 
saluto = 'Ciao'
nuovo_saluto = 'M' + saluto[1:]
print(saluto, nuovo_saluto)

# ricerca


def trova(parola, lettera, indice):
    indice = indice
    while indice < len(parola):
        if parola[indice] == lettera:
            return indice
        indice = indice+1
    return -1


print(trova('pippo', 'p', 0))

# contatore

parola = 'banana'
conta = 0
for lettera in parola:
    if lettera == 'a':
        conta = conta + 1
print(conta)


def contaparole(lettera_input, parola_input):
    conta = 0
    for lettera in parola_input:
        if lettera == lettera_input:
            conta = conta + 1
    print(conta)


contaparole('n', 'ottone')


def conta_parole_input():
    lettera_input = input('Inserisci la lettera : \n')
    parola_input = input('Inserisci la lettera : \n')
    conta = 0
    for lettera in parola_input:
        if lettera == lettera_input:
            conta = conta + 1
    print(conta)


# conta_parole_input()

# upper/lower
parola_minuscolo = input('Inserisci la parola\n')
lettera = str(input('Inserisci la lettera\n'))
parola_maiuscola = parola_minuscolo.upper()
parola_trasf_minuscola = parola_maiuscola.lower()
#print(parola_maiuscola, parola_trasf_minuscola)
# find
indice = parola_minuscolo.find(lettera)
# print(indice)

nome = 'bob'
# lettera, parte dalla posizione 1 e arriva alla 3 quindi la parola b che troverà sara la seconda
ricerca = nome.find('b', 1, 3)
print(ricerca)


uno = 'a' in 'banana'
due = 'c' in 'maggiore'

print(uno, due)  # true, false

# stampo le lettere che esistono in entrambe le parole


def entrambe(parola_uno, parola_due):
    for lettera in parola_uno:
        if lettera in parola_due:
            print(lettera)


entrambe('ciao', 'ciaone')  # c,i,a,o


# stampo le lettere che esistono in entrambe le parole
def entrambe():
    parola_uno = input('Inserisci la prima parola\n')
    parola_due = input('Inserisci la seconda parola\n')

    for lettera in parola_uno:
        if lettera in parola_due:
            print(lettera)


entrambe()


def frase():
    prima_parola = input('Inserisci la prima parola\n')
    seconda_parola = input('Inserisci la seconda parola\n')
    if prima_parola < seconda_parola:
        print('La tua parola ' + prima_parola +
              ' ,viene prima di ' + seconda_parola)
    elif prima_parola > seconda_parola:
        print('La tua parola ' + prima_parola +
              ' ,viene dopo ' + seconda_parola)
    else:
        print('Tutto ok ' + seconda_parola)


frase()


