import random

def busquedaBinaria(lista,inicio,final, objetivo):
    if inicio>final:
        return False
    
    medium = (inicio+final)//2

    if lista[medium] == objetivo:
        return True
    elif lista[medium]<objetivo:
        return busquedaBinaria(lista,medium+1,final,objetivo)
    else:
        return busquedaBinaria(lista,inicio,final-1,objetivo)


if __name__ =='__main__':
    tamano_lista = int(input("De qué tamaño es la lista: "))
    objetivo = int(input("Qué número desea encontrar: "))

    lista =sorted([random.randint(0,100) for i in range (tamano_lista)])

    encontrado = busquedaBinaria(lista,0,len(lista),objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"}')