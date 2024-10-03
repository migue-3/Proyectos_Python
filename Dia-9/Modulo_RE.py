import re

texto = "Si necesitas ayuda llama al (658)-598-997 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra)

# -- como lo hariamos con expresiones regulares ? ---- #
patron = "ayuda"
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())
# ---- Para encontrar la palabras mas de una vez --- #
busqueda_todo = re.findall(patron, texto)
print(busqueda_todo)
print(len(busqueda_todo))

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
# --- Mas ejemplos un poco mas abstractos de RE ----- #
texto2 = "llama al 247-247-6989 ya mismo"
patron2 = r"\d\d\d-\d\d\d-\d\d\d\d"
resultado = re.search(patron2, texto2)
print(resultado)
print(resultado.group())

patron_cuantificado = r"\d{3}-\d{3}-\d{4}"
resultado_cuantificado = re.search(patron_cuantificado, texto2)
print(resultado_cuantificado)
print('esteeeeeeee',resultado_cuantificado.group())

patron_compilado = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
resultado_compilado = re.search(patron_compilado, texto2)
print(resultado_compilado.group(3))

# -- ejemplo de uso practico en una contraseña con caracteres de digito y alfanumericos ---- #
clave = input("Ingrese su contraseña: ")
patron_clave = r'^\D{1}\w{7}$'
chequear = re.search(patron_clave, clave)
print(chequear)
# ---- ejemplo de una RE con operadores especiales ----- #
texto3 = "No atendemos los lunes por la tarde"
buscar = re.search(r'lunes|martes', texto3)
buscar2 = re.search(r'demos', texto3)
print(buscar)
print(buscar2)
buscar3 = re.search(r'.demos', texto3)
print(buscar3)
buscar4 = re.search(r'....demos', texto3)
print(buscar4)
buscar5 = re.search(r'....demos...', texto3)
print(buscar5)

