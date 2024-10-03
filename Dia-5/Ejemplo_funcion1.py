precios_cafe = [('Latte', 2.50), ('Capucchino', 2.20), ('Negrito', 1.50)]


# Ejemplo de como 'Desempacar' tupples
# for cafe,precio in precios_cafe:
#     print(cafe, precio)

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)


print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es el {cafe} y cuesta {precio}$")
