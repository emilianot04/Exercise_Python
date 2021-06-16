
#Ogni volta che sperimentate una nuova caratteristica, dovreste provare ad inserire degli errori. Ad esempio, nel programma “Ciao, mondo!”, cosa succede se dimenticate uno dei due apici? O entrambi? O se scrivete sbagliato print?
# print('ciao Mondo)
# Syntax error
# print(ciao Mondo)
# Syntax error invalid Syntax
#sprint('ciao Mondo')
#name not definited


#1. In un’istruzione di stampa, cosa succede se dimenticate una delle parentesi, o entrambe?
# print'ciao mondo'
# Syntax error


#2. Se state cercando di stampare una stringa, cosa succede se dimenticate uno degli apici, o entrambi?
# print(ciao Mondo')
#IndentationError: unexpected indent

#3. Per rendere negativo un numero, gli si antepone un segno meno, come in -2. Cosa succede se anteponete un segno più ad un numero? E nel caso di 2++2?
#print(2+-2)
# risultato 0
#print(2++2)
# risultato 4

#4. Nella notazione matematica, gli zeri iniziali sono ammessi, come in 02. In questo caso, cosa succede in Python?
# print(02)
# SyntaxError: leading zeros in decimal intege
#5. Cosa succede se scrivete due valori, senza inserire in mezzo un operatore?
#print (2 2)
#SyntaxError: invalid syntax

#Esercizio 1.2. Avviate l’interprete di Python e utilizzatelo come calcolatrice.
#1. Quanti secondi ci sono in 42 minuti e 42 secondi?
# print(42*60+42)
# Risultato 2562

#2. Quante miglia ci sono in 10 chilometri? Suggerimento: un miglio equivale a 1,61 km.
# print(10*1.61)
# Risultato 16,1
#3. Se correte una gara di 10 chilometri in 42 minuti e 42 secondi, qual è la vostra cadenza media (tempo per miglio in minuti e secondi)? Qual è la vostra velocità media, in miglia all’ora?
secondi = 42*60+42
print(secondi)
km_miglio = 10*1.61
print(km_miglio)

miglio_secondi=(secondi/km_miglio)

print(miglio_secondi)
miglio_minuti=(miglio_secondi/60)
print(miglio_minuti)
print(secondi/60/60)
vm_sec= print(km_miglio*(secondi/60/60))

#11.457833333333335 miglia all'ora
