palabra = 'python'
# lista = []
# for letra in palabra:
#     lista.append(letra)
# print(lista)

# MISMO RESULTADO PERO MAS EFICIENTE ##
# lista = [letra for letra in palabra]
# lista = [num if num * 2 > 10 else 'no' for num in range(0,21,2)]
# print(lista)

# EJEMPLO DE USO MAS EN LA VIDA REAL
pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)
