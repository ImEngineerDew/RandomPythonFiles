def diccionario():
    dic_base = {}

    while True:
        DNI = int(input("Ingrese su DNI por favor: "))
        nombre = input("Ingrese su nombre, por favor: ")

        dic_datos_per = {}
        dic_datos_per["Nombre"] = nombre 
        dic_datos_per["DNI"] = DNI
        
        dic_base[DNI] = dic_datos_per

        opc = input("Desea agregar otro dato (SI/NO): ").upper()

        if(opc == 'NO'):
            break
    print(dic_base)
            

if __name__ == '__main__':
    diccionario()