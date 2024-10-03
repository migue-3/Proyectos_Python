from pathlib import Path

# Ruta absoluta al directorio principal del usuario actual
# base = Path.home()
#
# guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_familia.txt"))

# Para apuntar a otro archivo seleccionando la misma ruta de "guia"
# guia2 = guia.with_name("La_pedrera.txt")
# print(base)
# print(guia)
# print(guia.parent.parent)
# print(guia2)

# Para enumerar todos los archivos .txt que hay en el directorio de Europa
# guia = Path(Path.cwd(), "Europa")
# Usamos el "**/" para que nos muestre todos los archivos txt que hay en el directorio
# Europa incluyendo los que estan en los subdirectorios
# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)

# Para calcular rutas que esten relacionadas entre si con el metodo "relativeTo"
guia = Path("Europa", "España", "Barcelona", "Sagrada familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)


