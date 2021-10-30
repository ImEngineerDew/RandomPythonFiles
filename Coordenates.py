class Coordenates:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    
    def distance(self, otraCoordenada):
        x_diff = (self.x - otraCoordenada.x)**2
        y_diff = (self.y - otraCoordenada.y)**2

        return (x_diff+y_diff)*0.5

if __name__ == '__main__':
    coord1 = Coordenates(3,30)
    coord2 = Coordenates(4,8)

    print(coord1.distance(coord2))