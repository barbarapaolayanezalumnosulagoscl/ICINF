def sumatoria(numero):
    if numero == 1:
        return 1
    else:
        return numero + sumatoria(numero - 1)

numero = 5
resultado = sumatoria(numero)
print("La sumatoria de los números hasta", numero, "es:", resultado)
