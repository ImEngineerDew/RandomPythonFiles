def matrix():
    nombres = []
    apellidos = [] 
    week = []
    sumatory = []

    #The quantity of the elements that may be introduced by keyboard
    quantity = int(input("Please write the quantity of data to input (write 0 to exit): "))  

    if (quantity >0):        
        for i in range(quantity):
            ingresar_nombre = input("Type your name:\t")
            ingresar_apellido = input("Type your surname:\t")

            #Space for adding names and surnames
            nombres.append(ingresar_nombre)
            apellidos.append(ingresar_apellido)

            monday     = int(input("km traveled on monday:\t"))
            tuesday    = int(input("km traveled on tuesday:\t"))
            wednesday  = int(input("km traveled on wednesday:\t"))
            thrusday   = int(input("km traveled on thrusday:\t"))
            friday     = int(input("km traveled on friday:\t"))
            saturday   = int(input("km traveled on saturday:\t"))
            sunday     = int(input("km traveled on sunday:\t"))   
        
            #Space for adding the kilometers per hoy traveled by day
            week.append([monday,tuesday,wednesday,thrusday,friday,saturday,sunday])
            
            #This line makes the sum of the days traveled on km
            suma_semanas = monday+tuesday+wednesday+thrusday+friday+saturday+sunday

            sumatory.append(suma_semanas)

            for i,j,k,l in zip(nombres,apellidos,week,sumatory):
                print(i,j,"\t",k,"\t",l)  
    else:
        print("End of the program!")
          
if __name__ == '__main__':
    matrix()
