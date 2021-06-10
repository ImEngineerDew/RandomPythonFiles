def cadenas():    
    
    nombres = input("Ingrese un nombre comprendido entre 6 y 12 carácteres: ")
    cuenta = len(nombres)

    while True:                                                      #también puede ser usada la siguiente instrucción "while cuenta>=6 or cuenta<=12" 
        if(len(nombres)<6):
            print("Nombre: "+nombres+", y es menor de seis letras")
            nombres = input("Ingrese un nombre comprendido entre 6 y 12 carácteres: ")
        elif (len(nombres)>12):
            print("Nombre: "+nombres+", y es mayor de seis letras")
            nombres = input("Ingrese un nombre comprendido entre 6 y 12 carácteres: ")
        else:
            print("Nombre: "+nombres+", el nombre está entre 6 y 12 letras")  
            break                                                     #Este break se pone para evitar ejecuciones infinitas

if __name__ == '__main__':
    cadenas()