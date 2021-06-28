def conteo(inicio):    
    if inicio>0:
        inicio=-1
        print(inicio)
        conteo(inicio)
    else:
        print("Ende!!!")
    print ("Cuenta", inicio)
       

if __name__ == '__main__':
    cuenta = int(input("Ingrese el conteo ascendente: "))
    #limite = int(input("Ingrese el conteo límite: "))

    conteo(cuenta)
