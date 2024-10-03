# def suma(*args):
#     # total = 0
#     # for arg in args:
#     #     total += arg
#     # return total
#     return sum(args)
#
# print(suma(2,3,5,45,6))
#
#
# def suma_cuadrados(*args):
#     suma = 0
#     for arg in args:
#         suma += arg ** 2
#
#     return suma


def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'

print(numeros_persona('miguel',2,6))