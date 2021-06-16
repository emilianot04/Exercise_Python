#esercizio 9.3  Scrivete una funzione di nome evita che richieda una parola e una stringa di lettere vietate, e restituisca True se la parola non contiene alcuna lettera vietata.
#Modificate poi il programma in modo che chieda all’utente di inserire una stringa di lettere vietate, e poi stampi il numero di parole che non ne contengono alcuna. Riuscite a trovare una combinazione di 5 lettere vietate che escluda il più piccolo numero di parole?


##

def evita(parola,vietate):

 for lettera in parola:
    if lettera in vietate:
        return False
    return True

            

print(evita('ciao', 'i'))

