# mi_bool = 4 < 5 > 6
# print(mi_bool)

# mi_bool = 4 < 5 and 5 > 6
# mi_bool = (4 > 2) and (5 == 2+3)
# mi_bool = (55 == 55) and ("Perro" == 'Perro')
# print(mi_bool)
#
# mi_bool1 = 4 < 5 or 5 > 6
# print(mi_bool1)

# texto = "Esta frase es breve"
# mi_bool = ("frase" in texto) and ("phyton" in texto)
# mi_bool = ("frase" in texto) or ("phyton" in texto)
# print(mi_bool)

# mi_bool = not (5 == 5)
# print(mi_bool)
# mi_bool1 = not (5 != 5)
# print(mi_bool1)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not(palabra1 in frase) and not(palabra2 in frase)
print(mi_bool)