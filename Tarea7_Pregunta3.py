supermercado = {}

while True:
    producto = input("Ingrese el nombre del producto (presione enter para finalizar): ")
    if not producto:
        break  
    cantidad = int(input("Ingrese la cantidad (valor) de "+producto+": "))
    supermercado[producto] = cantidad

X = float(input("Ingresa un valor numérico X: "))


print("Productos en el supermercado")
for producto, cantidad in supermercado.items():
    cantidad_multiplicada = cantidad * X
    print(producto + ":", cantidad_multiplicada)