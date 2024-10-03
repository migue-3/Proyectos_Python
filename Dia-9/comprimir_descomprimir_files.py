import zipfile
import shutil

# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
# --- PARA AGREGAR LOS LOS ARCHIVOS QUE QUEREMOS COMPRIMIR A 'mi_zip' --- #
# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')
# mi_zip.close()
# --- PARA DESCOMPRIMIR LOS ARCHIVOS LO HACEMOS ASI --- #
# zip_descomprimir = zipfile.ZipFile('archivo_comprimido.zip', 'r')
# zip_descomprimir.extractall()

# -- otro manera para descomprimir y comprimir archivos pero con el modulo shutil --- #
# -- comprimir todo lo que contenga una carpeta o directorio --- #
# ruta_carpeta_origen = 'C:\\Users\\miguel.escalante\\Desktop\\Carpeta_superior'
# archivo_destino = 'Todo_Comprimido'
# shutil.make_archive(archivo_destino, 'zip', ruta_carpeta_origen)

# para descomprimir con shutil ---- #
shutil.unpack_archive('Todo_Comprimido.zip', 'C:\\Users\\miguel.escalante\\Desktop\\Extraccion Terminada', 'zip')
