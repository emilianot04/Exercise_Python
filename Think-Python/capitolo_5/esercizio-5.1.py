import time
import datetime

tempo = time.time()

print(tempo)
anno = 365*24*60*60

anni_passati = int(tempo/anno)
print('anni passati:' + str(anni_passati))

mesi_resto = anni_passati % 12
print('mese passati:' + str(mesi_resto))

giorni_resto = mesi_resto % 30

print('giorno attuale:' + str(giorni_resto))

ore_resto = tempo % (365*24*60*60)
print('ora attuale:' + str(ore_resto))

giorni_passati = int(tempo % (365))
print('giorni passati :' + str(giorni_passati))


""" giorno_secondi = 24*60*60
secondi = tempo/giorno_secondi
print(secondi) """
""" minuti = ore/60
print(minuti)
secondi = minuti/60
print(secondi) """
""" 
print(tempo/365)
print(tempo/(365*24))
print(tempo/(365*24*60))
print(tempo/(365*24*60*60)) """
