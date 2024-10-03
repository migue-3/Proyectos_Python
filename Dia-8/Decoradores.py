# este codigo es una pequeña introduccion para entender como trabajan los decoradores
# def cambiar_letras(tipo):
#     def mayuscula(texto):
#         print(texto.upper())
#
#     def minuscula(texto):
#         print(texto.lower())
#
#     if tipo == "may":
#         return mayuscula
#     elif tipo == "min":
#         return minuscula
#
#
# operacion = cambiar_letras("may")
# operacion("maduro vete ctm")

# Aca empieza el codigo utilizando los DECORADORES
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion


# @decorar_saludo
def mayuscula(texto):
    print(texto.upper())


# @decorar_saludo
def minuscula(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada("maduro hp")









