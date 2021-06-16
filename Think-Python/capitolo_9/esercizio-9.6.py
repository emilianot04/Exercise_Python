# Esercizio 9.6. Scrivete una funzione di nome alfabetica che restituisca True se le lettere di una parola compaiono in ordine alfabetico (le doppie valgono). Quante parole “alfabetiche” ci sono?

def alfabetica(parola):

    if len(parola):
        return True
    if parola[0]>parola[1]:
        return False
    return alfabetica(parola[1:])

            

print(alfabetica('flossy'))

