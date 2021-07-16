import json

pokeTrainer = { }
listTrainer = [ ]

def addTrainer(trainerID,trainerName,trainerAge,pokeID):
    global pokeTrainer,listTrainer

    localPokeTrainer = { }

    while True:
        
        localPokeTrainer["Trainer ID"] = trainerID
        localPokeTrainer["Name"]       = trainerName
        localPokeTrainer["Age"]        = trainerAge
        localPokeTrainer["Pókemon ID"] = pokeID
        
        pokeTrainer[trainerID]    = localPokeTrainer

        listTrainer.append(localPokeTrainer) 
        break

def showTrainer(trainerID):
    print(pokeTrainer.get(trainerID))

#----------------This function can print all the PokeTrainers (it's a list)----------------------#
def showAllTrainers():
    with open("My Python Samples/AllTrainers.txt",'w') as file:
        counter = 1
        for listado in listTrainer:
            file.write(str(listado))
            cont=+1
            #print(listado)

#----------------------function to erasing pokeTrainers---------------------------#
def removeTrainer(trainerID):
    pokeTrainer.pop(trainerID)
    print("The trainer has been removed")   

def menu():
    while True:
        print("""--------Listado de opciones--------
                1. Adding a PokeTrainer
                2. Delete a PokeTrainer
                3. Find a PokeTrainer (Requires an ID Trainer)
                4. Print a list of all PokeTrainers (Its could export a .txt file) 
                5. Pokemon Battle!
                6. Close the app!""")      

        try:
            option = int(input("Please choose a valid option from the list: "))

            if (option == 1):
                listPoke = [ ] 
                while True:
                    try:
                        idTrainer    = int(input("Please write your Trainer ID: "))
                        nameTrainer  = input("Please write your name: ")
                        ageTrainer   = int(input("Please write your age: "))
                        for pk in range(0,4):
                            idPoke = int(input("Please type your pokemon ID: "))
                            listPoke.append(idPoke)                                                    
                        addTrainer(idTrainer,nameTrainer,ageTrainer,listPoke)
                        break
                    except ValueError:
                        print("Try again!")

            elif (option == 2):
                pass
            elif (option == 3):
                while True:
                    try:
                        showID = int(input("Please write your id Trainer: "))
                        showTrainer(showID)
                        break
                    except ValueError:
                        print("Try Again")
            elif (option == 4):
                showAllTrainers()
            elif (option == 5):
                pass
            elif (option == 6):
                print("End of the program...")
                return False
                break
        except ValueError:
            print("Please choose a valid option from the list: ")



if __name__ == '__main__':
    menu()




