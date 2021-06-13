def datos_ingresados():
        
    listado = []    
   
    while True:       
        datos = int(input("Ingrese un número que no sea menor a cero: ")) 
        if(datos>0):
            listado.append(datos)      
        else:
            print("Fin del programa")
            break
    print("Datos ingresados: "+str(listado))

if __name__ == '__main__':
    datos_ingresados()
