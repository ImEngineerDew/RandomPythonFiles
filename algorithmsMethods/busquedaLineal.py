import random

def busquedaLineal(lista,objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ =='__main__':
    tamano_lista = int(input("De qué tamaño es la lista: "))
    objetivo = int(input("Qué número desea encontrar: "))

    lista =[random.randint(0,100) for i in range (tamano_lista)]

    encontrado = busquedaLineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"}')