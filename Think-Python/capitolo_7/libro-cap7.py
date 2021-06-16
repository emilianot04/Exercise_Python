#While

def contoallarovescia(n):
    while n > 0:
        print(n)
        n = n-1
    print('Via!')

contoallarovescia(6)


while True:
    riga = input('> ')
    if riga == 'fine':
        break
    print(riga)
print('Finito!')