def una_minuscola1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
def una_minuscola2(s):
    for c in s:
        if 'c'.islower(): #errore
            return 'True'
        else:
            return 'False'
def una_minuscola3(s):
    for c in s:
        flag = c.islower()
    return flag
def una_minuscola4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
def una_minuscola5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(una_minuscola1('ciao Sono PipppPPPP')) #True
print(una_minuscola2('ciao Sono PipppPPPP')) #True
print(una_minuscola3('ciao Sono PipppPPPP')) #False
print(una_minuscola4('ciao Sono PipppPPPP')) #True
print(una_minuscola5('ciao Sono PipppPPPP')) #False