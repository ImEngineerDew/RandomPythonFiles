def mostrar_lista(lista_productos):
    for producto in lista_productos:
        print(producto[0],producto[1],producto[2])

def impuesto():
    lista_productos = [["ps5",3000000],["ordenador",2000000],["cascos",400000]]

    #
    mostrar_lista(lista_productos)

    #cada sublista puede verse como un índice en la lista mayor
    seleccion =  input("Ingrese un elemento que está en la lista de productos: ")

    #producto es la sublista
    for producto in lista_productos:
        if(producto[0]==seleccion):
            VAT = producto[1]*0.19
            print(VAT)

if __name__ == '__main__':
    impuesto()