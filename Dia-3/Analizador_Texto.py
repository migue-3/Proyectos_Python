texto = input("Ingrese tu texto para analizar: ").lower()
letras = []
# texto = texto.())()

letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS QUE TIENE MI TEXTO")
palabras = texto.split()
print(f"Hemos encontrado '{len(palabras)}' palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"Letra del inicio es '{letra_inicio}' y la letra del final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
texto_invertido = texto[::-1]
print(texto_invertido)

print("\n")
print("BUSCANDO LA PALABRA PHYTON")
buscar_phyton = "phyton" in texto
dic = {
    True: "si",
    False: "no"
}
print(f"La palabra 'phyton' {dic[buscar_phyton]} se encuentra en el texto")

