#esercizio 9.1 Scrivete un programma che legga il file words.txt e stampi solo le parole composte da più di 20 caratteri (caratteri spaziatori esclusi).

fin = open('words.txt')
parola = fin.readline() 
for riga in fin:
    parola_len = len(riga)
    if (parola_len > 20) :
        print (riga)

