
def funzione(s):
    print(s)


def fai2volte(funzione, valore):
  funzione(valore)
  funzione(valore)


fai2volte(print , 'spam')

print('--------------------')


def fai4volte(funzione, valore):
    fai2volte(funzione,valore)
    fai2volte(funzione,valore)


fai4volte(print , 'spam')
