palabras = []

while True:
    palabra = input("ingrese Palabras (presione enter para terminar): ")
    if palabra == "":
        break
    palabras.append(palabra)

print("\nNúmero de letras 'A' o 'a' en cada palabra:")
for palabra in palabras:
    contador_a = 0
    for letra in palabra:
        if letra == 'A' or letra == 'a':
            contador_a += 1

    contador = ""
    if contador_a == 0:
        contador = "0"
    elif contador_a == 1:
        contador = "1"
    elif contador_a == 2:
        contador = "2"
    elif contador_a == 3:
        contador = "3"
    elif contador_a == 4:
        contador = "4"
    elif contador_a == 5:
        contador = "5"
    elif contador_a == 6:
        contador = "6"
    elif contador_a == 7:
        contador = "7"
    elif contador_a == 8:
        contador = "8"
    elif contador_a == 9:
        contador = "9"

    print(palabra + ": " + contador)