total_preguntas = int(input("Ingrese el total de preguntas: "))
preguntas_correctas = int(input("Ingrese la cantidad de preguntas contestadas correctamente: "))
porcentaje_correctas = (preguntas_correctas / total_preguntas) * 100
if porcentaje_correctas >= 95:
            nivel = "Nivel máximo"
elif porcentaje_correctas >= 70:
            nivel = "Nivel medio"
elif porcentaje_correctas >= 40:
            nivel = "Nivel regular"
else:
    nivel = "Fuera de nivel"

print("Porcentaje de respuestas correctas: ",porcentaje_correctas,"%")
print("Nivel:",nivel)
