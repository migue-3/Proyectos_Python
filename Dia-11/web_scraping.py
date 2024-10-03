import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
# print(resultado.text)
# sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# print(sopa.select('title'))
# print(len(sopa.select('span')))
# print(sopa.select('h1'))
# print(sopa.select('title')[0].getText())

# parrafo_especial = sopa.select('span')[4].getText()
# print(parrafo_especial)
# print(sopa.select(".copyright")[0].getText())

resultado_wiki = requests.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
sopa = bs4.BeautifulSoup(resultado_wiki.text, 'lxml')
print(sopa.select("#Otros_proyectos_de_la_Fundación_Wikimedia")[0].getText())
