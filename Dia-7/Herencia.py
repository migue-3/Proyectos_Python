class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):
    pass


piolin = Pajaro(3, 'negro')
piolin.nacer()
print(piolin.color, piolin.edad)
# __bases__ me dice de quien esta heredando la clase pajaro
# print(Pajaro.__bases__)
# Subclases me dice a quien esta heredando la clase animal
# print(Animal.__subclasses__())




