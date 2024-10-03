# diccionario = {
#     'c1':'valor1',
#     'c2':'valor2'
# }
# print(type(diccionario))
# print(diccionario)
# resultado = diccionario['c1']
# print(resultado)

# cliente = {
#     'nombre':'juan',
#     'apellido':'Bermudez',
#     'peso': 245,
#     'talla':'XXXL',
#     'altura':1.78
# }
# consulta = cliente['apellido']
# print(consulta)

# dic = {
#     'c1':55,
#     'c2':[10,20,30],
#     'c3':{'s1':100,'s2':200}
# }
# print(type(dic['c2']))
# print(dic['c2'])
# print(dic['c2'][0])
# print(dic['c3']['s2'])

# dic = {
#     'c1':['a','b','c'],
#     'c2':['d','e','f']
# }
#
# print(dic['c2'][1].upper())

dic = {
    1:'a',
    2:'b'
}

dic[3]='c'  #Para agg un nuevo elemento a la lista
dic[2]='B'  #Para sobreescribir en la lista
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())