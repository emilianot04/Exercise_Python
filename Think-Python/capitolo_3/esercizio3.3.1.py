piu = '+'
meno = '-'
pipe = '|'
space = ' '

prima_riga = ((space + meno)*4 + space)


def riga_piu():
    print(piu + prima_riga + piu + prima_riga + piu)

def riga_pipe():
    print((pipe + (space*9))*2 + pipe)

def riga_pipe_4():    
    riga_pipe()
    riga_pipe()
    riga_pipe()
    riga_pipe()

def blocco():
    riga_piu()
    riga_pipe_4()


def stampa():
    blocco()
    blocco()
    riga_piu()

stampa()
