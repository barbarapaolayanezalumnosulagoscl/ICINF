nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")
nombres = [nombre1, nombre2]
nombres.sort()
print("Nombres ordenados alfabéticamente:")
for nombre in nombres:
    print(nombre)