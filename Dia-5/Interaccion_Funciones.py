from random import *
# Lista inicial
palitos = ['-', '----', '--', '---']


# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle al usuario un intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)


# Comprobar el resultado
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos!!')
    else:
        print('Esta vez te has salvado..')

    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)


lista_numeros = [1, 2, 15, 7, 2, 8]
print(list(set(lista_numeros)))
lista_numeros.sort()
print(lista_numeros.pop(-1))


def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista


def promedio(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio


def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado


def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista




