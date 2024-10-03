import os
from pathlib import Path

# ruta = os.getcwd()
# print('getcwd-->> ' + ruta)
#
# ruta = os.chdir('C:\\Users\\miguel.escalante\\Desktop\\chdirtestPY')
# archivo = open('texto.txt')
# print(archivo.read())
#
### Para crear una nueva carpeta en el ruta especificada ###
# ruta = os.makedirs('C:\\Users\\miguel.escalante\\Desktop\\chdirtestPY\\otra')

# ruta = 'C:\\Users\\miguel.escalante\\Desktop\\python\\pythonProject\\Dia-6\\prueba.txt'
# elemento = os.path.basename(ruta)
# directorio = os.path.dirname(ruta)
# print(elemento + '\n', directorio)
# todo_junto_tuppla = os.path.split(ruta)
# print(todo_junto_tuppla)

### Para eleminar un directorio ###
# ruta = 'C:\\Users\\miguel.escalante\\Desktop\\chdirtestPY\\otra'
# os.rmdir(ruta)

### Para leer un archivo en una ruta distinta ###
# otro_archivo = open('C:\\Users\\miguel.escalante\\Desktop\\chdirtestPY\\texto.txt')
# print(otro_archivo.read())

### Para crear rutas que sean interpretadas por cualquier sistema operativo ###
carpeta = Path('C:/Users/miguel.escalante/Desktop/chdirtestPY')
archivo = carpeta / 'texto.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())







