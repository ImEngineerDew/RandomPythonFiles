def matrix():
    nombres = []
    apellidos = [] 
    week = []
    sumatory = []    

    try:
        #The quantity of the elements that may be introduced by keyboard
        quantity = int(input("Please write the quantity of data to input (write 0 to exit): "))     
       
        while True:
            if (quantity !=0):        
                for i in range(quantity):
                    ingresar_nombre = input("Type your name: ")
                    ingresar_apellido = input("Type your surname: ")

                    #Space for adding names and surnames
                    nombres.append(ingresar_nombre)
                    apellidos.append(ingresar_apellido)

                    try:
                        monday     = int(input("km traveled on monday: "))
                        tuesday    = int(input("km traveled on tuesday: "))
                        wednesday  = int(input("km traveled on wednesday: "))
                        thrusday   = int(input("km traveled on thrusday: "))
                        friday     = int(input("km traveled on friday: "))
                        saturday   = int(input("km traveled on saturday: "))
                        sunday     = int(input("km traveled on sunday: "))   
        
                        #Space for adding the kilometers per hoy traveled by day
                        week.append([monday,tuesday,wednesday,thrusday,friday,saturday,sunday])
            
                        #This line makes the sum of the days traveled on km
                        suma_semanas = monday+tuesday+wednesday+thrusday+friday+saturday+sunday

                        sumatory.append(suma_semanas)
                        
                        for i,j,l in zip(nombres,apellidos,sumatory):
                            print(i,j," = ",l) 

                    except (ValueError,UnboundLocalError):
                        print("You've had written a string, as well as that the append is out!")
                break
            else:
                print("End of the program!")
                break

    except ValueError:
        print("You've written the string chain!")
  
if __name__ == '__main__':
    matrix()
