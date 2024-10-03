# Funcion para verificar si el numero ingresado tiene 3 cifras
# def chequear_3_cifras(numero):
#     return numero in range(100,1000)
#

def chequear_3_cifras(lista):
    lista_3_cifras = []
    for num in lista:
        if num in range(100,1000):
            # return True
            lista_3_cifras.append(num)
        else:
            pass
    # Ponemos el return false al mismo nivel del for, para decirle a la funcion que ya
    # salimos del loop if, y pueda responder correctamente False si se da el caso
    # return False
    return lista_3_cifras


resultado = chequear_3_cifras([247,459,109,34,1,67,99,1924])
print(resultado)

lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]


def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True


def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma


def cantidad_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad




