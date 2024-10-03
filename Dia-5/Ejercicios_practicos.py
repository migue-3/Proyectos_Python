# def devolver_distintos(a,b,c):
#     suma = a+b+c
#     lista = [a,b,c]
#
#     if suma > 15:
#         return max(lista)
#     elif suma < 10:
#         return min(lista)
#     else:
#         lista.sort()  # Para ordenar la lista de menor a mayor
#         return lista[1] # Esto nos devuelve el valor del medio
# print(devolver_distintos(2,4,10))


# def letras_unicas(palabra):
#     mi_set = set()  # Creamos un set vacio
#     for letra in palabra:
#         mi_set.add(letra)
#     mi_lista = list(mi_set)  # Hacemos el casting convirtiendolo a una list para poder ordenarlo alfabeticamente.
#     mi_lista.sort()  # Ordemanos alfabeticamente
#
#     return mi_lista

# print(letras_unicas('aaeeiioouu'))


def chequear_ceros(*args):
    contador = 0

    for arg in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(chequear_ceros(3,5,6,7,5,7,6,0,4,6,4,3,6,4,6,4,0))





