def datos_ingresados():

    opc = ' '    
    listado = []    
   
    while True:       
        datos = int(input("Ingrese un número que no sea menor a cero: ")) 
        if(datos>0):
            listado.append(datos)      
        else:
            opc= input("Desea ordenar los datos: Y/N: ")
            if(opc=='Y'):
                listado.sort()
                print("Datos ingresados: "+str(listado))
                print("Fin del programa")
                break
            else:
                print("Datos ingresados: "+str(listado))
                print("Fin del programa")
                break
    

if __name__ == '__main__':
    datos_ingresados()
