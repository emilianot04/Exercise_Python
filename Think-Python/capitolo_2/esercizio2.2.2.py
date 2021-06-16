prezzo_copertina = 24.95
sconto_libreria = (40/100)
spedizione_prima_copia = 3
spedizione_altre_copie = 0.75

prezzo_libreria = prezzo_copertina*sconto_libreria
totale_spedizioni = 59*spedizione_altre_copie + spedizione_prima_copia

totale = prezzo_libreria*60 + totale_spedizioni

print(totale)


# 646.050
