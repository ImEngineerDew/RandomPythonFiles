import json

list_pokemons = [ ]

#open a json file
with open ("My Python Samples/pokedex.json", encoding = "utf8") as jsonFile:
    list_pokemons = json.load(jsonFile)

#ordering alphabeticalment
list_pokemons.sort(key=lambda p: p["name"]["english"])

for dictionary_poke in list_pokemons:
    print(dictionary_poke["id"]," - ",dictionary_poke["name"]["english"])

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


#find a pokemon

pokeAdd = [ ]
p=1

for pokeList in range (0,5):
    while True:
        poke_find = input("Please write your pokemon: ")
        encontro, id_pokemon  = binaryPoke(list_pokemons,poke_find)
        if encontro == True:
            pokeAdd.append(poke_find)
            p=+1
        else:
            print("This pokemon doesn't exist in that JSON file!")
        break
print(pokeAdd)







