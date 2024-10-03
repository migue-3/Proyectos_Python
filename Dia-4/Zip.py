nombres = ['Miguel','Ana','Valeria']
edades = [18,23,34]
ciudades = ['Lima','Caracas','Buenos aires']

combinados = list(zip(nombres,edades,ciudades))
print (combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")