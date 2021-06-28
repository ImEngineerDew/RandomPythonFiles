def can(quantity):
    
    listado = []

    for i in range(0,quantity):
        opcion = input("Seleccione la opción de datos para agregar (str para cadenas/int para numeros): ").lower()
        if(opcion == 'str'):
            datos = input("Ingrese los datos de la lista: ")
            listado.append(datos)
        elif(opcion == 'int'):
            datos = int(input("Ingrese los datos de la lista: "))
            listado.append(datos)
    print(listado)


if __name__ == '__main__':
    cantidad = int(input("Ingrese el limite de datos en la lista: "))
    can(cantidad)

