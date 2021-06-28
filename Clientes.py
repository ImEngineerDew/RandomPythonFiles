def add_client():  

    global main_list,personal_list

    while True:
        name    = input("Ingrese su nombre, por favor: ")
        DNI     = int(input("Ingrese su DNI, por favor: "))
        address = input("Ingrese su dirección, por favor: ") 
        phone   = int(input("Ingrese su número de teléfono, por favor: "))
        mail    = input("Ingrese su correo por favor: ")
        preferences = input("¿Su cliente es preferente: (Y/N)?").upper()    
        show_preferences(preferences)    

        personal_list["Nombre"] = name
        personal_list["DNI"] = DNI
        personal_list["Dir"] = address
        personal_list["Tel"] = phone
        personal_list["email"] = mail
        personal_list["Preferente"] = preference

        main_list[DNI] = personal_list

        opc = input("Desea agregar otro dato (SI/NO): ").upper()

        if(opc == 'NO'):
            break 

def erase_client():
    pass

def show_unique_client():
    pass

def show_all_clients():
    global main_list
    print(main_list)

def show_preferences(preference):
    if (preference == 'Y'):
        return True
    elif (preference == 'N'):
        return False

def menu():

    while True:

        print("""--------Listado de opciones------------
                1. Añadir cliente
                2. Borrar un cliente
                3. Mostrar un cliente
                4. Mostrar todos los clientes 
                5. Mostrar sólo los clientes preferentes
                6. Finalizar el programa""")
    
        opcion = int(input("Seleccione una opción de la lista: "))   
    
        if(opcion == 1):
            add_client()           
        elif(opcion == 2):
            erase_client()
        elif(opcion == 3):
            show_unique_client()
        elif (opcion == 4):
            show_all_clients()
        elif (opcion == 5):
            show_preferences()
        elif(opcion == 6):
            print("Fin del programa!")
            return False
            break
        

if __name__ == '__main__':

    main_list = { }
    personal_list ={ }
    menu()
