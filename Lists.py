def Lists():

        Tierra =  [['España', 'Portugal', 'Francia', 'Paises Bajos', 'Alemania'], 
        ['Colombia', 'Ecuador', 'Perú', 'Chile', 'Argentina']]

        for ame, euro in zip(Tierra[0],Tierra[1]):
            print(euro,":\t",ame)

if __name__ == '__main__':
    Lists()