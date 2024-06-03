palabras = []

while True:
    palabra = input("Ingresa una palabra (o presiona Enter para finalizar): ")
    if not palabra:
        break
    palabras.append(palabra)

for palabra in palabras:
    num_vocales = 0
    num_consonantes = 0
    for letra in palabra:
        if letra.isalpha():
            if letra.lower() in "aeiou":
                num_vocales += 1
            else:
                num_consonantes += 1
    print(palabra,": Vocales =", num_vocales," Consonantes = ",num_consonantes)