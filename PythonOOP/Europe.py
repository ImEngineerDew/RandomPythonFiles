class Europe:
    def __init__(self,nameCountry,habitants,HDI,currency):
        self.nameCountry = nameCountry
        self.habitants = habitants
        self.HDI = HDI
        self.currency = currency

class europeanUnion(Europe):
    def __init__(self, nameCountry,habitants,HDI,currency,belongsEU,belongsEurozone):
        super().__init__(nameCountry,habitants,HDI,currency)
        self.belongsEU = belongsEU
        self.belongsEurozone = belongsEurozone


class CEI(Europe):
    def __init__(self, nameCountry, habitants, HDI, currency, belongsCEI, belongsFormerUSSR):
         super().__init__(nameCountry,habitants,HDI,currency)
         self.belongsCEI = belongsCEI
         self.belongsFormerUSSR


if __name__ == '__main__':

    print("1.  Unión Europea")
    print("2.  Comunidad de estados independientes (exURSS)")
    print("3.  Salir del programa")
    opcion =  int(input("Seleccione que tipo de organización pertenece a un estado europeo: "))
    
    if (opcion == 1):
        randomEU = europeanUnion("Germany",83190656,0.947,'Euro','yes','yes')

        randomEU.nameCountry = input("Ingrese el nombre del pais: ")
        randomEU.habitants   = int(input("Ingrese los habitantes del pais: "))
        randomEU.HDI         = float(input("Ingrese su IDH: "))
        randomEU.currency    = input("Ingrese la moneda: ")          

    elif (opcion == 2):
        pass
    elif (opcion == 3):
        print("Fin del programa")
    



