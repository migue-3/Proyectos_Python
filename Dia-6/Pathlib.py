from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/miguel.escalante/Desktop/python/pythonProject/Dia-6/prueba.txt')
ruta_windows = PureWindowsPath(carpeta)
# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)

if not carpeta.exists():
    print('El archivo que intentas abrir no existe')
else:
    print(carpeta.name)
    print(ruta_windows)

