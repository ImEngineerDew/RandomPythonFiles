def excepciones():
    #try:
    #    while(1==1):
    #        quantity = int(input("Please write the quantity of data to input (write 0 to exit): "))  
    #        if(quantity>0): 
    #            break
    #except ValueError:
    #    print("Only positive numbers")

    listado = []
    sumatoria = []
    
    try:
        while True:
            for i in range(0,7):
                alpha = int(input("Ingrese los datos a sumar: "))
                listado.append(alpha)
                suma = sum(listado)  
                sumatoria.append(suma)           
                
            print("Total suma = ",sumatoria[i])
            break
    except ValueError:
        print("You don't put negative numbers")

    

    

if __name__ == '__main__':
    excepciones()