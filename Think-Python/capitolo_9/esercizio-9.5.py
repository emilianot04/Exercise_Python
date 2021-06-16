#Esercizio 9.5. Scrivete una funzione di nome usa_tutte che richieda una parola e una stringa di lettere richieste e che restituisca True se la parola utilizza tutte le lettere richieste almeno una volta. Quante parole ci sono che usano tutte le vocali aeiou? E aeiouy?

def usa_tutte(parola,richieste):

 for lettera in richieste:
    if lettera not in parola:
        return False
    return True

            

print(usa_tutte('ciao', 'e'))

