def tuplas():
    mi_lista = [ ]

    for i in range(0,5):
        agregar = input("Ingrese un elemento para agregar: ")
        mi_lista.append(agregar)
        mi_tupla= tuple(mi_lista)
    print(mi_tupla)


if __name__ == '__main__':
    tuplas()

