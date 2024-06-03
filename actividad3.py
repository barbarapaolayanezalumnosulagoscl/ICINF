alturas = [] 
altura = float(input("Ingrese la altura en metros (0 para finalizar): "))
while altura != 0:
            alturas.append(altura)
            altura = float(input("Ingrese la altura en metros (0 para finalizar): "))
if len(alturas) > 0:
    promedio = sum(alturas) / len(alturas)
    print("Altura promedio:",promedio," metros")
else:
     print("No se ingresaron alturas.")