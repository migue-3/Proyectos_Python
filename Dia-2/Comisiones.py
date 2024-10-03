nombre = input("Dime tu nombre: ")
ventas = input("¿Cuanto hiciste en ventas este mes? :")
ventas = float(ventas)
comisiones = round(ventas * 13 / 100, 2)

print(f"Hola {nombre}, este mes generaste en comisiones $$: {comisiones}")
