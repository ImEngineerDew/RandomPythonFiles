#Nota para el tutor: main_list es el diccionario primario en dónde se guarda la key primaria 
#quién corresponde al NIF

main_list = {}
products = ' '

#----------------------function to adding clients-----------------------#
def add_client(name,DNI,address,phone,mail,preferences):
    global main_list,products

    while True:
                            
        personal_list ={} 
        
        personal_list["Nombre"] = name
        personal_list["DNI"] = DNI
        personal_list["Dir"] = address
        personal_list["Tel"] = phone
        personal_list["email"] = mail
        personal_list["Preferente"] = preferences
        personal_list["Goods"] = products

        add_products(products)

        #The secondary dictionary must to be attached to the main dictionary, here this 
        main_list[DNI] = personal_list
        break   

#----------------------function to erasing clients---------------------------#
def erase_client(DNI):
    main_list.pop(DNI)
    print("Entrada eliminada")    

#----------------------function to show unique clients-----------------------#   
def show_unique_client(DNI):
    print(main_list.get(DNI))   

#----------------------function to show all clients--------------------------#
def show_all_clients():
    for clave, valor in main_list.items():
        print(clave,"=",valor)

#-------------------function to show only prefrent clients-------------------#
def show_preferences(preferences):
    for clave, valor in main_list.items():
        if valor["Preferente"] == 'Y':
            print(str(valor["Nombre"])+" - "+str(valor["DNI"]))

def add_products(products):
    my_list = [ ]
    my_list.append(products)
                
  
def menu():

    while True:
        print("""--------Listado de opciones--------
                1. Añadir cliente
                2. Borrar un cliente
                3. Mostrar un cliente
                4. Mostrar todos los clientes 
                5. Mostrar sólo los clientes preferentes
                6. Agregar productos al carrito de compras
                7. Finalizar el programa""")

        try:
            opcion = int(input("Seleccione una opción de la lista: "))   
    
            if(opcion == 1):
                while True:
                    try:
                        NIF     = int(input("Ingrese su NIF, por favor: "))
                        nombre    = input("Ingrese su nombre, por favor: ")        
                        direccion = input("Ingrese su dirección, por favor: ") 
                        telefono   = int(input("Ingrese su número de teléfono, por favor: "))
                        correo    = input("Ingrese su correo por favor: ")
                        preferencias = input("¿Su cliente es preferente: (Y/N)?").upper()
                        add_client(nombre,NIF,direccion,telefono,correo,preferencias) 
                        break
                    except ValueError:
                        print("¡Por favor intente de nuevo!")          
            elif(opcion == 2):
                while True:
                    try:
                        CC= int(input("Ingrese su NIF, por favor: "))
                        erase_client(CC)
                        break
                    except ValueError:
                        print("¡Ingrese de nuevo el NIF")
            elif(opcion == 3):
                while True:
                    try:
                        CC = int(input("Ingrese su NIF, por favor: "))
                        show_unique_client(CC)
                        break
                    except ValueError:
                        print("¡Ingrese de nuevo el NIF!")
            elif (opcion == 4):
                show_all_clients()
            elif (opcion == 5):
                preferente = input("¿El cliente es preferente: ?").upper()
                show_preferences(preferente)
            elif (opcion == 6):
                cantidad = int(input("Ingrese la cantidad de productos a agregar: "))
                for i in range(0,cantidad):
                    tipo_productos = input("Ingrese los productos a agregar: ")
                    add_products(tipo_productos)                
            elif(opcion == 7):
                print("Fin del programa!")
                return False
                break
        except ValueError:
            print("¡Por favor intente de nuevo!")
        

if __name__ == '__main__':   
    menu()
