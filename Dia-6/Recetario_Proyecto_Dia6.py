import os
import shutil
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), 'Recetas')


def contar_recetas(ruta):
    contador = 0
    for archivo_txt in Path(ruta).glob('**/*.txt'):
        contador += 1
    return contador


def inicio():
    # Mostrar menu de inicio
    system('cls')
    print('\n')
    print('*' * 50)
    print('*' * 5 + ' Bienvenido al administrador de recetas ' + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentran en el directorio --> {mi_ruta}")
    print(f"Total de recetas --> {contar_recetas(mi_ruta)}")
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elije una opcion --> ')
        print('''
        [1] - Leer receta
        [2] - Crear nueva receta
        [3] - Crear nueva categoria
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input('Seleccione una opcion correcta desde el 1 hasta el 6 --> ')
    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    # ITERAMOS DENTRO DEL DIRECTORIO POR CADA CARPETA QUE ENCUENTRE EN LA RUTA
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoria --> ")
    # Restamos - 1 para obtener el indice correcto de la categoria
    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print("Recetas --> ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta --> ")
    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta --> ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta")
        descripcion_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, descripcion_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Esa receta ya existe en nuestra base de datos")


def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoria --> ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Esa categoria ya existe en nuestra base de datos")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    # metodo para eliminar directorios (carpetas) (solo funciona si carpeta esta vacia)
    # Path(categoria).rmdir()
    shutil.rmtree(categoria) # metodo para eliminar directorios (carpetas) y sus archivos dentro
    print(f"La categoria {categoria.name} ha sido eliminada")


def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresion 'V' para volver al menu --> ")


finalizar_programa = False

while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            # elegir recetas
            mi_receta = elegir_recetas(mis_recetas)
            # elegir recetas
            leer_receta(mi_receta)
        # volver al inicio
        volver_inicio()
    elif menu == 2:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # Crear receta nueva
        crear_receta(mi_categoria)
        # volver al inicio
        volver_inicio()
    elif menu == 3:
        # crear categoria nueva
        crear_categoria(mi_ruta)
        # volver al inicio
        volver_inicio()
    elif menu == 4:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            # elegir recetas
            mi_receta = elegir_recetas(mis_recetas)
            # eliminar receta
            eliminar_receta(mi_receta)
        # volver al inicio
        volver_inicio()
    elif menu == 5:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # eliminar categoria
        eliminar_categoria(mi_categoria)
        # volver al inicio
        volver_inicio()
    elif menu == 6:
        # finalizar programa
        finalizar_programa = True





