class CocheNuevo:
    largoChasis = 500
    anchoChasis = 400
    ruedas = 4
    enMarcha = False

    def arranca(self,arrancamos):
        self.enMarcha = arrancamos
        if (self.enMarcha):
            return "El coche está en marcha"
        else:
            return "Está detenido"
    
    def marcaCoche(self):
        marca = input("Escriba la marca del coche")
        print("La marca del coche es: "+marca)
    
         


if __name__ == '__main__':
    miCoche = CocheNuevo()

    print("Largo chasis: "+str(miCoche.largoChasis))
    miCoche.arranca(False)
    miCoche.marcaCoche()
    
