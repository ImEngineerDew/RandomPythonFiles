class Europe:
    def __init__(self,nameCountry,habitants,HDI,currency):
        self.nameCountry = nameCountry
        self.habitants = habitants
        self.HDI = HDI
        self.currency = currency

class europanUnion(Europe):
    def __init__(self, nameCountry,habitants,HDI,currency,belongsEU,belongsEurozone):
        super().__init__(nameCountry,habitants,HDI,currency)
        self.belongsEU = belongsEU
        self.belongsEurozone = belongsEurozone


class CEI(Europe):
    def __init__(self, nameCountry, habitants, HDI, currency, belongsCEI, belongsFormerUSSR):
         super().__init__(nameCountry,habitants,HDI,currency)
         self.belongsCEI = belongsCEI
         self.belongsFormerUSSR




