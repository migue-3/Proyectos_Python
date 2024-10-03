class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        # self.edad = edad
        # self.color = color
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('PÍO')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')


# piolin = Pajaro(2,'amarillo', 600)
# piolin.nacer()
# piolin.hablar()
# mi_animal = Animal(5, 'negro')

# EJEMPLO DE HERENCIA MULTIPLE
class Padre:
    def hablar(self):
        print("Regaño")


class Madre:
    def reir(self):
        print('ja ja ja')

    def hablar(self):
        print("Vengan a comer")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
# Te indica el orden en que se resuelven los metodos heredados "__mro__"
print(Nieto.__mro__)
