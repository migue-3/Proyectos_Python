class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice muuuu')


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice beeeee')


vaca1 = Vaca("Marta")
oveja1 = Oveja("Nube")

# vaca1.hablar()
# oveja1.hablar()
# animales = [vaca1, oveja1]
#
# for animal in animales:
#     animal.hablar()


def animal_habla(animal):
    animal.hablar()


animal_habla(oveja1)


palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in palabra, lista, tupla:
    print(len(dato))


