# list = ['a','b','c','d']
# for letra in list:
#     numero_letra = list.index(letra) + 1
#     print(f"Letra: {numero_letra} - {letra}")

# lista = ['luis', 'julia', 'luli', 'carlos', 'martina']
#
# for nombre in lista:
#     if nombre.startswith('l'):
#         print(nombre)
#     else:
#         print("Nombre que no comienza con l")

# numeros = [1,2,3,4,5]
# mi_valor = 0
#
# for num in numeros:
#     mi_valor = mi_valor + num
#     print(mi_valor) ##IMPORTANCIA DE LA TABULACION DEL PRINT OJO##

palabra = "phyton es genial"

# for letra in 'palabra':
#     print(letra)

# for letra in [1,2,3]:
#     print(letra)

# for letra in (14,'ab'):
#     print(letra)

# for objeto in [[1, 2], ['hola', 3], [4, 5]]:
#     print(objeto)

# for a,b in [[1, 2], ['hola', 3], [4, 5]]:
#     print(a)
#     print(b)

mi_dic = {
    'clave1': 'a',
    'clave2': 'b',
    'clave3': 'c',
}

for item in mi_dic.items():
    print(item)