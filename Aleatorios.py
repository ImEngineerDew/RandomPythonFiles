import random
import math

def aleatorios():  

    listado = [ ]  
    squares = [ ]
    cubics  = [ ]
    
    for i in range(0,10):
        valor = int(random.random()*10.0)
        listado.append(valor)
        squares.append(int(math.pow(valor,2)))
        cubics.append(int(math.pow(valor,3)))

    print("Lista original: "+str(listado))
    print("Cuadrados: "+str(squares))
    print("Cubos: "+str(cubics))
   

if __name__ == '__main__':
    aleatorios()
    