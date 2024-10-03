# if 10 > 9:
#     print("Es correcto")

# x = True
# if x:
#     print("Correcto")

# if 5==2:
#     print("correcto")
# else:
#     print("incorrecto")

# mascota = "perro"
# if mascota == "gato":
#     print("Tienes un gato")
# elif mascota == "perro":
#     print("Tienes un perro")
# else:
#     print("no puedo saber que animal tienes")

# edad = 16
# calificacion = 6.5
# if edad < 18:
#     print("Eres menor de edad")
#     if calificacion >= 7:
#         print("Aprobado")
#     else:
#         print("Reprobado")
# else:
#     print("Eres adulto")
#

# edad = 16
# tiene_licencia = False
#
# if (edad >= 18) and (tiene_licencia == True):
#     print("Puedes conducir")
#     if (edad >= 18) and (tiene_licencia == False):
#         print("No puedes conducir. Necesitas contar con una licencia")
# elif edad < 18:
#     print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

habla_ingles = True
sabe_python = False

if (habla_ingles == True) and (sabe_python == True):
    print("Cumples con los requisitos para postularte")
elif sabe_python == False:
        print("Para postularte, necesitas saber programar en Python")
elif habla_ingles == False:
        print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")