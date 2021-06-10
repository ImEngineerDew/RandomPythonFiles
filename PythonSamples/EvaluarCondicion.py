def evaluacion(asientos):
    if asientos == 'si':
        return True
    else:
        return False

def condicional_evaluacion():
    tiene_asientos = input("Tiene asientos de cuero: ")
    asientos_cuero = evaluacion(tiene_asientos)
    if asientos_cuero == True:
        print("El coche tiene asientos de cuero")
    else:
        print("El coche no tiene asientos de cuero")
    

if __name__ == '__main__':
    condicional_evaluacion()
