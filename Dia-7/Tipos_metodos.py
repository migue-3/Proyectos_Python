class Pajaro:

    alas = True

    # Metodos de instancia de la clase
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pío mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    # Metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        cls.alas = False
        print(f"Puso {cantidad} huevos {cls.alas}")

    # Metodo estatico
    @staticmethod
    def mirar():
        print("El pajaro mira")


# piolin = Pajaro("amarillo", "canario")
# piolin.pintar_negro()
# piolin.volar(45)
# piolin.alas = False
# print(piolin.alas)
Pajaro.poner_huevos(6)
Pajaro.mirar()