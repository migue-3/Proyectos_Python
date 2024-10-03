from datetime import datetime, date

# ------ Horas --------------------- #
# mi_hora = datetime.time(14, 31)
# print(type(mi_hora))
# print(mi_hora.hour)
# print(mi_hora.minute)
# print(mi_hora)
# ------ Fechas --------------------- #
# mi_dia = datetime.date(2024, 8, 13)
# print(mi_dia)
# print(mi_dia.year)
# print(mi_dia.ctime())
# print(mi_dia.today())
# ------ Fechas / Horas --------------------- #
mi_fecha = datetime(2025, 11, 19, 22, 10, 15, 4566)
print(mi_fecha)

mi_fecha = mi_fecha.replace(month=12)
print(mi_fecha)

nacimiento = date(1995, 12, 31)
defuncion = date(2095, 6, 19)
vida = defuncion - nacimiento
print(vida)
print(vida.days)

despierta = datetime(2022, 10, 5, 7, 30)
durmio = datetime(2022, 12, 5, 23, 59)
vigilia = durmio - despierta
print(vigilia)
print(vigilia.seconds)
print(vigilia.days)