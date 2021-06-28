#Nota para el tutor: main_list es el diccionario primario en dónde se guarda la key primaria 
#quién corresponde al NIF

main_list = {}

def add_client():
    global main_list

    while True:
        try:
            DNI     = int(input("Ingrese su DNI, por favor: "))
            name    = input("Ingrese su nombre, por favor: ")        
            address = input("Ingrese su dirección, por favor: ") 
            phone   = int(input("Ingrese su número de teléfono, por favor: "))
            mail    = input("Ingrese su correo por favor: ")
            preferences = input("¿Su cliente es preferente: (Y/N)?").upper()      
                
            personal_list ={} 
        
            personal_list["Nombre"] = name
            personal_list["DNI"] = DNI
            personal_list["Dir"] = address
            personal_list["Tel"] = phone
            personal_list["email"] = mail
            personal_list["Preferente"] = preferences

            main_list[DNI] = personal_list
            break
        except ValueError:
            print("¡Por favor intente de nuevo!")


def erase_client(DNI):
    main_list.pop(DNI)
    print("Entrada eliminada")    
    
def show_unique_client(DNI):   
    print(main_list.get(DNI))   

def show_all_clients():
    for i, j in main_list.items():
        print(i,"=",j)

def show_preferences(preferences):
     if preferences == 'Y':
        print (main_list.get(preferences))
        return True
     elif preferences == 'N':
        return False      
  
def menu():

    while True:
        print("""--------Listado de opciones--------
                1. Añadir cliente
                2. Borrar un cliente
                3. Mostrar un cliente
                4. Mostrar todos los clientes 
                5. Mostrar sólo los clientes preferentes
                6. Finalizar el programa""")

        try:
            opcion = int(input("Seleccione una opción de la lista: "))   
    
            if(opcion == 1):
                add_client()           
            elif(opcion == 2):
                CC= int(input("Ingrese su DNI, por favor: "))
                erase_client(CC)
            elif(opcion == 3):
                CC = int(input("Ingrese su DNI, por favor: "))
                show_unique_client(CC)
            elif (opcion == 4):
                show_all_clients()
            elif (opcion == 5):
                preferente = input("¿El cliente es preferente: ?").upper()
                show_preferences(preferente)
            elif(opcion == 6):
                print("Fin del programa!")
                return False
                break
        except ValueError:
            print("¡Por favor intente de nuevo!")
        

if __name__ == '__main__':   
    menu()
