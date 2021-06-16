# Una funzione che chiama se stessa si dice ricorsiva e la procedura che la esegue è detta ricorsione.


def stampa_n(s, n):
    if n <= 0:
        # l’istruzione di ritorno return provoca l’uscita dalla funzione.
        return
    print(s)
    stampa_n(s, n-1)


stampa_n(10, 5)

# 5.11 input
testo = input()
testo

nome = input('come ti chiami? \n')
nome

prompt = input('come ti chiami? \n')
velocita = input(prompt)

prompt2 = 'velocità\n'
velocita2 = input(prompt2)
int(velocita2)