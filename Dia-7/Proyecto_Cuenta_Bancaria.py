class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f"Cliente: {self.nombre} {self.apellido}\n"
                f"Balance de cuenta {self.numero_cuenta}: ${self.balance}\n")

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito exitoso!!")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro exitoso!!")
        else:
            print("No cuentas con el monto suficiente en tu balance para hacer este retiro")


def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print("Elige:\nPara depositar (D)\nPara retirar (R)\nPara salir (S)")
        opcion = input()
        if opcion == "D":
            monto_dep = int(input("Ingrese el monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == "R":
            monto_ret = int(input("Ingrese el monto que desea retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Gracias por operar con Banco Phyton!! vuelva pronto..")
















