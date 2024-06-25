deudores = {}

for x in range(5):
    rut = input("Ingrese el Rut de la persona: ")
    deuda = float(input("Ingrese la deuda en pesos: "))
    deudores[rut] = deuda


while True:
    rut_abono = input("Ingresa el Rut de la persona para abonar (enter para terminar): ")
    if not rut_abono:
        break  
    abono = float(input("Ingresa el monto del abono en pesos: "))

    if rut_abono in deudores:
        deudores[rut_abono] -= abono
        if deudores[rut_abono] <= 0:
            del deudores[rut_abono]  

print("\nPersonas deudoras")
for rut, saldo in deudores.items():
    print("RUT:", rut, "Saldo de deuda:", saldo, "pesos")