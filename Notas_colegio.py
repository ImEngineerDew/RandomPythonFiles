def notas():

    lista_calificaciones = [ ]
    
    for i in range (0,5):
        notas = float(input("Ingrese las notas a calificar: "))
        lista_calificaciones.append(notas)
        suma_notas = sum(lista_calificaciones)
        promedio = suma_notas/(len(lista_calificaciones))   
        nota_mayor = max(lista_calificaciones)     
        nota_menor = min(lista_calificaciones)

    print("\n")
    print("Notas: "+str(lista_calificaciones))
    print("Suma: "+str(suma_notas))
    print("Promedio: "+str(promedio))
    print("Nota mayor: "+str(nota_mayor))
    print("Nota menor: "+str(nota_menor))

if __name__ == '__main__':
    notas()