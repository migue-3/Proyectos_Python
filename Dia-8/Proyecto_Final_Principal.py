import Proyecto_Final_Numeros


def preguntar():
    print("Bienvenidos a Farmacia Phyton")
    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmética\n")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    Proyecto_Final_Numeros.decorador(mi_rubro)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()











