import random

def ordenar_random():

    listado = []

    for i in range (0,10):
        valor = int(random.random()*10.0)
        listado.append(valor)
        listado.sort()
    print("Lista ordenada: "+str(listado))
   

if __name__ == '__main__':
    ordenar_random()