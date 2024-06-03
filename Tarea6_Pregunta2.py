mi_lista = []

while True:
    print("\nMenú de opciones:")
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista según el índice")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista según el dato (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        mi_lista.append(elemento)
        print("Elemento",elemento," agregado a la lista.")
    elif opcion == "2":
        try:
            indice = int(input("Ingrese el índice del elemento a modificar: "))
            nuevo_valor = input("Ingrese el nuevo valor: ")
            mi_lista[indice] = nuevo_valor
            print("Elemento en el índice ",indice," modificado.")
        except IndexError:
            print("Índice fuera de rango. Intente nuevamente.")
    elif opcion == "3":
        try:
            indice = int(input("Ingrese el índice del elemento a eliminar: "))
            elemento_eliminado = mi_lista.pop(indice)
            print("Elemento ",elemento_eliminado," eliminado de la lista.")
        except IndexError:
            print("Índice fuera de rango. Intente nuevamente.")
    elif opcion == "4":
        if mi_lista:
            elemento_eliminado = mi_lista.pop()
            print("Elemento ",elemento_eliminado," eliminado de la lista.")
        else:
            print("La lista está vacía.")
    elif opcion == "5":
        buscar_elemento = input("Ingrese el elemento a buscar: ")
        try:
            indice = mi_lista.index(buscar_elemento)
            print("El elemento ",buscar_elemento," se encuentra en el índice", indice,".")
        except ValueError:
            print("El elemento ",buscar_elemento,"no está en la lista.")
    elif opcion == "6":
        print("Elementos en la lista:")
        for i, elemento in enumerate(mi_lista):
            print(i,":" ,elemento)
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
