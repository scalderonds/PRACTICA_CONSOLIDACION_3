"""INSTRUCCIONES
Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la
prueba de acuerdo con lo solicitado.

DESCRIPCIÓN

Dada la siguiente lista de nombres:
• Harry Houdini
• Newton
• David Blaine
• Hawking
• Messi
• Teller
• Einstein
• Pele
• Juanes

Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
frase ‘El gran‘ antes del nombre de cada mago.

Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
lista.

Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes."""


listanombres = ["Harry Houdini", "Newton", "David Blaine",
                "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

magos = []
cientificos = []
otros = []


def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]


def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)


for nombre in listanombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

hacer_grandioso()

print("LISTA COMPLETA DE NOMBRES:")
imprimir_nombres(listanombres)
print("\nMAGOS:")
imprimir_nombres(magos)
print("\nCIENTIFICOS:")
imprimir_nombres(cientificos)
print("\nOTROS:")
imprimir_nombres(otros)
