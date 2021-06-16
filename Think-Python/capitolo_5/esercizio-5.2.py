
def verifica_fermat(a,b,c,n):

    primo_blocco = (a**n) + (b**n) == c**n
    
    if  ( primo_blocco == True) :
        print('Santi Numi, Fermat si è sbagliato!')
    else:
        print('No, questo non è vero.')



verifica_fermat(3,4,5,2)


# 2. Scrivete una funzione che chied aall’utentediinserirevaloridia,b,cen,liconvertaininteri e usi verifica_fermat per controllare se violano il teorema di Fermat.##

a = int(input('valore a\n'))
b= int(input('valore b\n'))
c = int(input('valore c\n'))
n = int(input('valore n\n'))

verifica_fermat(a,b,c,n)