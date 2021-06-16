fin = open('words.txt')
parola = fin.readline()
# print(parola)

for riga in fin:
    parola = riga.strip()
    print(parola) 


