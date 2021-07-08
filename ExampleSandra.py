
def añadir_cliente(nif,nombre, direccion, telefono, correo, preferente, baseDatos): 
    dic_cliente= {}
    upd_add = False
    if len (baseDatos)>=0:
        baseDatos [nif] = {"nombre":nombre, "direccion": direccion, "telefono": telefono, "correo": correo, "preferente":preferente}
    return upd_add

def eliminar_cliente (nif,baseDatos):
    if (nif in baseDatos):
        opcion_borrar= int(input("ingrese 1 si esta seguro de borrarlo: "))
        if (opcion_borrar== 1):
            del baseDatos[nif]
            
            
def mostrar_cliente (baseDatos):
    print(baseDatos)
    for clave,valor in baseDatos.items():
        print("Nombre:{} - Direccion:{} - Tel:{} - Correo:{} - ¿Es preferente?:{}".format(clave, valor["nombre"],valor["direccion"],valor["telefono"], valor["correo"],valor["preferente"]))
        
def listas_all_cliente (baseDatos):
    for clave,valor in baseDatos.items():
        print(clave,valor["nombre"])
        
def lista_cliente_preferentes (baseDatos):
    for clave,valor in baseDatos.items():
        if valor["preferente"]:
            print(clave,valor["nombre"])

def main():
    dic_baseDatos={}
    while True:
        print ("""
        ........................................................
                     BASE DE DATOS DE NUESTROS CLIENTES
        ........................................................

            1. Añadir cliente
            2. Eliminar cliente
            3. Mostrar cliente
            4. Listar todos los clientes
            5. Listar clientes preferentes
            6. Terminar
        ........................................................
            """)
        try:
            opcion = int(input("Elija una de las opcion: "))
        
            if opcion == 1:

               
                nif= int(input("Ingrese el nif del cliente  a agregar: "))
                nombre= input("Nombre del cliente: ").lower()
                direccion= input("dirección: ").lower()
                telefono= int(input("telefono: "))
                correo = input("correo: ").lower()
                preferente= input("¿Es un cliente preferente? (escriba SI o NO): ").lower()

              
                if (preferente == 'si'):
                    preferente_guardar= True
                elif (preferente== 'no'):
                    preferente_guardar= False 
                else:
                    print ("Por favor escriba una opcion valida  ")

                       
                add_upd = añadir_cliente(nif, nombre, direccion, telefono, correo, preferente, dic_baseDatos)
                print(dic_baseDatos)

               
            elif opcion == 2:
                
                nif_eliminado= input("Ingrese el NIF del cliente: ")
                eliminar_cliente(nif,dic_baseDatos)

            elif opcion ==3:
                mostrar_cliente(dic_baseDatos)

            elif opcion == 4:  
                 listas_all_cliente(dic_baseDatos) 

            elif opcion ==5:
                lista_cliente_preferentes(dic_baseDatos)

            if opcion ==6:
                break
            else:
                print ("El cliente no existe")
                
        except ValueError:
            print ("Ops! solo puede ingresar una opción válida")
            
if __name__ == "__main__":
    main()
