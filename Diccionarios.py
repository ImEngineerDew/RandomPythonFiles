def dictionaries():

    datos ={"NOMBRE": 'Dewin', "Edad": 28, 
            "Profesion":'Ingeniero electrónico',
            "Cursos":['Python','Java','Kotlin']}

    
    pais = {"Nombre:":'España',"Población:":47500000,"PIB per cápita:": 450000 }

    for i,j in pais.items():
        print(i,j)
    #print(datos.items())

    #for clave,valor in datos.items():
    #    print(clave," - ",valor)

    

if __name__ == '__main__':
    dictionaries()