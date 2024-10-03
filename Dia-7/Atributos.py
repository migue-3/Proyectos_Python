class Pajaro:
    # ATRIBUTOS DE CLASE, SON LOS QUE DEFINIMOS PARA TODOS LOS OBJETOS DE MI CLASE PAJARO
    alas = True

    # DEFINIMOS EL METODO CONSTRUCTOR PARA ASIGNARLE ATRIBUTOS A NUESTRA CLASE PAJARO
    # DENTRO DE LOS () PASAMOS LOS PARAMETROS Y LA PALABRA RESERVADA SELF
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro("azul", 'loro')
print(f"Mi pajaro es un {mi_pajaro.especie} {mi_pajaro.color}")
print(Pajaro.alas)
