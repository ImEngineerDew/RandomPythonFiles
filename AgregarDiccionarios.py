def diccionario():
    dic_base = {}

    while True:
        try:
            DNI = int(input("Ingrese su DNI por favor: "))
            nombre = input("Ingrese su nombre, por favor: ")
            preferente = input("¿El usuario es cliente preferente: ?")

            dic_datos_per = {}
            dic_datos_per["Nombre"] = nombre 
            dic_datos_per["DNI"] = DNI
            dic_datos_per["Cliente preferente: "] = preferente
        
            dic_base[DNI] = dic_datos_per

            opc = input("Desea agregar otro dato (SI/NO): ").upper()

            if(opc == 'NO'):
                break
        except ValueError:
            print("Try again!")
    for i, j in dic_base.items():
        print(i,"=",j)
            

if __name__ == '__main__':
    diccionario()