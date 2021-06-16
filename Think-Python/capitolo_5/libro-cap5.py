# operatore modulo
minuti = 105
print(minuti/60) #ore
print(minuti%60) #minuti

#booleani
#operatori logici (and, or, not)

#if (condizioni)

x= 1
if x > 0 :
    print('x è positivo')

#if else

y=5
if y%2 == 0 :
    print('y è pari')

else:
    print('y è dispari')


#if elif else:

if x< y:
    print('x è minore di y')
elif x>y:
    print('x è maggiore di y')
else:
    print('x e y sono uguali')


#Condizioni nidificate
if x == y:
    print('x e y sono uguali')
else:
    if x < y:
        print('x è minore di y')
    else:
        print('x è maggiore di y')

# Ricorsione
def contoallarovescia(n):
    if n <= 0:
        print('Via')
    else:
        print(n)
        contoallarovescia(n-1)

contoallarovescia(6)

# Una funzione che chiama se stessa si dice ricorsiva e la procedura che la esegue è detta ricorsione.


def stampa_n(s, n):
    if n <= 0:
        # l’istruzione di ritorno return provoca l’uscita dalla funzione.
        return
    print(s)
    stampa_n(s, n-1)


stampa_n(10, 5)

# 5.11 input
testo = input()
testo

nome = input('come ti chiami? \n')
nome

prompt = input('come ti chiami? \n')
velocita = input(prompt)

prompt2 = 'velocità\n'
velocita2 = input(prompt2)
int(velocita2)