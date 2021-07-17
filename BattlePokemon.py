import json
import os

pokeTrainer = { }
listTrainer = [ ]
listPokemons = [ ]

#-----------------------open a json file-----------------------------------#
with open ("My Python Samples/pokedex.json", encoding = "utf8") as jsonFile:
    list_pokemons = json.load(jsonFile)

#-------------------ordering alphabeticalment-------------------------------#
list_pokemons.sort(key=lambda p: p["name"]["english"])

#--------------------binary search for pokemons-----------------------------#

def binaryPoke(list_pokemons,name_poke):
    start = 0
    finish = (len(list_pokemons)-1)
    found = False

    found_id_poke = -1

    while (start<=finish and not found):
        #print(list_pokemons[middle]["name"]["english"].lower()," == ",name_poke.lower())

        middle = (start+finish)//2
        if list_pokemons[middle]["name"]["english"].lower()== name_poke.lower():
            found = True
            found_id_poke = list_pokemons[middle]["id"]
        else:
            if (name_poke < list_pokemons[middle]["name"]["english"].lower()):
                finish = middle -1 
            else:
                start = middle + 1

    return found,found_id_poke

#-------------------------Adding informations about of trainers-------------------#
def addTrainer(trainerID,trainerName,trainerAge,pokemons):
    global pokeTrainer,listTrainer,JSONPokemon

    localPokeTrainer = { }

    while True:
        
        localPokeTrainer["Trainer ID"] = trainerID
        localPokeTrainer["Name"]       = trainerName
        localPokeTrainer["Age"]        = trainerAge
        localPokeTrainer["Pókemon ID"] = pokemons

        pokeTrainer[trainerID]    = localPokeTrainer              
        listTrainer.append(pokeTrainer) 
        break

#------------Function that can find the trainerID-------------------------------#
def showTrainer(trainerID):
    print(pokeTrainer.get(trainerID))
    
#----------------This function can print all the PokeTrainers (it's a list)----------------------#
def showAllTrainers():
    with open("My Python Samples/AllTrainers.txt",'w') as file:
        for key, value in pokeTrainer.items():
            print(key," = ",value)        

#----------------------function to erasing pokeTrainers---------------------------#
def removeTrainer(trainerID):
    listTrainer.remove(pokeTrainer.pop(trainerID))
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
                pokeAdd = [ ] 
                p=1                
                while True:
                    try:
                        idTrainer    = int(input("Please write your Trainer ID: "))
                        nameTrainer  = input("Please write your name: ")
                        ageTrainer   = int(input("Please write your age: "))                

                        for poke in range(0,5):                           
                            poke_find = input("Please write your pokemon: ").lower()
                            encontro, id_pokemon  = binaryPoke(list_pokemons,poke_find)
                            if encontro == True:
                                pokeAdd.append(poke_find)
                                p=+1
                            else:
                                print("This pokemon doesn't exist in that JSON file!")
                                p=+1                                                                                                          
                        addTrainer(idTrainer,nameTrainer,ageTrainer,pokeAdd)
                        break
                    except ValueError:
                        print("Try again!")

            elif (option == 2):
                while True:
                    try:
                        idTrainer = int(input("Please write your Trainer ID: "))
                        removeTrainer(idTrainer)
                        break
                    except ValueError:
                        print("Try again!")
                        
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