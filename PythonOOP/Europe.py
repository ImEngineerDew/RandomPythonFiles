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
    #randomEU = europeanUnion("Germany",83190656,0.947,'Euro','yes','yes')

    opcion =  int(input("Seleccione que tipo de organización pertenece a un estado europeo: "))
    print("1.  Unión Europea")
    print("2.  Comunidad de estados independientes (exURSS)")

    



