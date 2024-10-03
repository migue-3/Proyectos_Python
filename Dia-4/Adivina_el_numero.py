from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input('Dime tu nombre: ')

print(f"Hola {nombre}, he pensado un numero entre 1 y 100\n"
      "Tienes 8 intentos para adivinar el numero")

while intentos < 8:
    estimado = int(input('¿Cual es el numero ganador? '))
    intentos += 1

    if estimado not in range(1,101):
        print('Tu numero esta por fuera del rango ganador que va desde 1 al 100')
    elif estimado < numero_secreto:
        print('Siga intentando, el numero es mas alto')
    elif estimado > numero_secreto:
        print('Siga intentando, el numero es mas bajo')
    else:
        print(f"Felicitaciones {nombre} has ganado!! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento se han agotado los intentos. El numero ganador era {numero_secreto}")
