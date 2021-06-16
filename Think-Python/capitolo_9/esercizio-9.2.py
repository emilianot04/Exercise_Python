#esercizio 9.2 Scrivete una funzione di nome niente_e che restituisca True se una data parola non contiene la lettera “e”.


##

def niente_e(parola):

 
    if  ('e' not in parola):
        return True
    else:
        return False
            

print(niente_e('ccccccccccceeee'))

##seconda parte
def niente_e_2(parola):
        esclusa = parola.replace('e', '')
        percentuale = (len(esclusa)/len(parola))*100
        final = str(percentuale) + '%'
        return 'parola finale : ' + esclusa , 'percentuale : ' + final 
            

print(niente_e_2('ccccccccccceeee'))