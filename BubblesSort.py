def bubbles_sort(listado):
    size_list = len(listado)-1
    
    for i in range(0,size_list):
        for j in range(0,size_list):
            if listado[j]>listado[j+1]:
                auxiliar = listado[j]
                listado[j] = listado[j+1]
                listado[j+1]=auxiliar
    return listado



if __name__ == '__main__':
    listado_numeros = [5,25,30,4,1,0,15,45,60,105,16,17,18,19]

    ordenar = bubbles_sort(listado_numeros)
    print(ordenar)