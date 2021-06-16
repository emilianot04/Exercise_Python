import math

def eval_ciclo():
    while True:
        dato = input('> ')
        if dato == 'fatto':
            break
        dato_number = int(dato)
        print(dato_number)
        ciclo_ev =  eval('math.sqrt(dato_number)')
        
        print(ciclo_ev)
    print(ciclo_ev)
    
eval_ciclo()
