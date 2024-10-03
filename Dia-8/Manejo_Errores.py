def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)


try:
    # Codigo que queremos probar
    suma()
except TypeError:
    # Codigo a ejecutar si sucede un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Eso no es un numero")
else:
    # Codigo a ejecutar si NO hay un eror
    print("Hiciste todo bien")
finally:
    # Codigo que se va a ejecutar de todos modos
    print("Eso fue todo")
##############################################################


def perdir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias has salido del loop while")


perdir_numero()

