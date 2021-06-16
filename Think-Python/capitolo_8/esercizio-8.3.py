def palindroma(parola):
    if  parola == parola[::-1]:
        return True
    else:
        return False

print(palindroma('otto')) #true
print(palindroma('radar'))#true
print(palindroma('pippo'))#false

