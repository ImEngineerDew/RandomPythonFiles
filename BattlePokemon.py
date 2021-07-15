import json

pokeTrainer = { }
listTrainer = [ ]

def addTrainer(trainerID,trainerName,trainerAge,pokeID):
    global pokeTrainer, listTrainer

    pokeTrainer["Trainer ID"] = trainerID
    pokeTrainer["Name"]       = trainerName
    pokeTrainer["Age"]        = trainerAge
    pokeTrainer["Pókemon ID"] = pokeID
    pokeTrainer[trainerID]    = trainerID
    
    listTrainer.append(pokeTrainer)


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
                pass
            elif (option == 2):
                pass
            elif (option == 3):
                pass
            elif (option == 4):
                pass
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




