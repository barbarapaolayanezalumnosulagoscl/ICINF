sueldo_minimo = 500000
sueldo_maximo = 1500000
contador_empleados = 0
contador_rango_bajo = 0
contador_rango_alto = 0
total_gasto = 0

while True:
    sueldo = float(input("Ingresa el sueldo del empleado (-1 para terminar): "))
    if sueldo == -1:
        break

    if sueldo >= sueldo_minimo and sueldo <= sueldo_maximo:
        contador_empleados += 1
        total_gasto += sueldo
        if sueldo <= 900000:
            contador_rango_bajo += 1
        else:
            contador_rango_alto += 1
    else:
        print("El sueldo ingresado no está dentro del rango válido.")
print("Empleados en el rango $500.000 - $900.000: ",contador_rango_bajo)
print("Empleados con sueldo mayor a $900.000: ",contador_rango_alto)
print("Gasto total de la empresa en sueldos: $",total_gasto)
