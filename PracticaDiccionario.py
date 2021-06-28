def diccionario(datos):   
    
    opcion = input("Desea modificar los datos en el diccionario: ").lower()
    
    while True:
        for i in range (0,3):
            if opcion == 'yes':
                elementos = input("¿Que valor desea modificar: ").lower()
                if elementos == 'nom':
                    datos['Pais'] = input("Escriba el nombre del país: ")
                elif elementos == 'pop':
                    datos['Poblacion'] = int(input("¿Cuánta población existe: ?"))
                elif elementos == 'pib':
                    datos['PIB'] = int(input("PIB percápita: ")) 
            elif opcion == 'no':
                break             
        for clave in datos:
            print(str(clave)+":"+str(datos[clave]))
        break

if __name__ == '__main__':

    pais = {'Pais':'España',
             'Poblacion':47450695,
             'PIB':31000}
             
    diccionario(pais)