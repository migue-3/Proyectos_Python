from collections import Counter, defaultdict, namedtuple

numeros = [2,3,4,2,4,7,4,7,4,2,1,9,6,9,2,3,6,7,5,8,8,8,2,3,1,4,5,6,7,8,9]
frase = "Menos chinos mas arroz"
print(Counter(numeros))
print(Counter("mississippi"))
print(Counter(frase.split()))
serie = Counter([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4])
print(serie.most_common())
print(list(serie))
# ---------------------------------------------------------- #
mi_dic = {"uno": "amarillo", "dos": "azul", "tres": "rojo"}
print(mi_dic["dos"])

mi_dic2 = defaultdict(lambda: "nada")
mi_dic2["uno"] = "verde"
print(mi_dic2["dos"])
print(mi_dic2)
# ------------------------------------------------------------- #
mi_tupla = (500, 247, 28)
print(mi_tupla[1])

Persona = namedtuple("Persona", ["nombre", "altura", "peso"])
ariel = Persona("ariel", 1.80, 92)
print(ariel.altura)