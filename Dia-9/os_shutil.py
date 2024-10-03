import os
import shutil
import send2trash


print(os.getcwd())
archivo = open("curso.txt", "w")
archivo.write("texto de prueba")
archivo.close()

print(os.listdir())
# ------COMO MOVER ARCHIVOS CON SHUTIL ------- #
# shutil.move("curso.txt", "C:\\Users\\miguel.escalante\\Desktop")

# ------COMO ELIMINAR ARCHIVOS CON SHUTIL OJO ESTE METODO ELIMINA CARPETAS Y ARCHIVOS------- #
# shutil.rmtree()

# --- eliminar archivos con send2trash ---- #
# send2trash.send2trash("curso.txt")

# --- Recorrer todos los directorios, carpetas, sub-carpetas y archivos --- #
# print(os.walk("C:\\Users\\miguel.escalante\\Desktop\\React"))

ruta = "C:\\Users\\miguel.escalante\\Desktop\\python\\pythonProject\\Dia-6"
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son : ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son: ")
    for arch in archivo:
        print(f"\t{archivo}")
    print("\n")
