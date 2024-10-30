

import random


def juego_adivinanza():
    numero_secreto = random.randint(1,100)
    intentos = 0 
    adivinado = False


    print('Bienvenido al juego de adivinanzas')
    print('Debes de adivinar un numero del 1 al 100')
    print('Intenta adivinarlo!!')

    while not adivinado:
        adivinanza = input('introduzca un numero del 1 al 100')

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f'El numero secreto es mayor a {adivinanza}')
            elif adivinanza > numero_secreto:
                print(f'El numero secreto es menor a {adivinanza}')

            else: 
                print(f'Felicitaciones has ganado! El numero es {adivinanza}')
        else:
            print('Por favor introduzca un numero valido entre 1 al 100')

juego_adivinanza()      