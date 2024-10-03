# def suma(**kwargs):
#     total = 0
#     # print(type(kwargs))
#     for clave,valor in kwargs.items():
#         print(f"{clave} = {valor}")
#         total += valor
#     return total
#
# print(suma(x=1, c=2, z=4))

# def prueba(num1, num2, *args, **kwargs):
#     print(f"El primer valor es {num1} ")
#     print(f"El segundo valor es {num2} ")
#
#     for arg in args:
#         print(f"arg = {arg}")
#
#     for clave,valor in kwargs.items():
#         print(f"{clave} = {valor}")
#
# prueba(2,4,3,4,6,2,x=3,z=4,f=24,7)
#
#
# # Práctica sobre Argumentos Indefinidos (*kwargs) 1
# def cantidad_atributos(**kwargs):
#     cantidad = 0
#     for clave in kwargs.items():
#         cantidad += 1
#     return cantidad
#
#
# # Práctica sobre Argumentos Indefinidos (*kwargs) 2
# def lista_atributos(**kwargs):
#     lista = []
#     for valor in kwargs.values():
#         lista.append(valor)
#     return lista


# Práctica sobre Argumentos Indefinidos (*kwargs) 3
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')


print(describir_persona("miguel", color_ojos='azul', color_pelo="negro"))

