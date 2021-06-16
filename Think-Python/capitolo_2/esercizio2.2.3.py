# 6:52 orario uscita
# 1 -5  miglio= 8' 15"
# 2-3-4 miglio = 7'12"


secondi = 15+12+12+12+15
# 66
minuti = 8+7+7+7+8
# 37

ore = 6

secondi_finali = secondi / 60
secondi_in_minuti = int(secondi % 60)

minuti_finali = int((52+minuti+secondi_finali) % 60)
minuti_in_ore = int((52+minuti+secondi_finali)/60)


orario_finale = ore + minuti_in_ore

nome = f"Arriverò alle ore {orario_finale} e {minuti_finali}"

print(nome)

# dopo le 07:30


