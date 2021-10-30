class DatosPersonales:
    def __init__ (self, nombre,edad,tipoSangre,altura):
        self.nombre = nombre
        self.edad = edad
        self.tipoSangre = tipoSangre
        self.altura = altura
    
    def info(self):
        print("Nombre: "+self.nombre)
        print("Edad: "+str(self.edad))
        print("Grupo sanguíneo: "+self.tipoSangre)
        print("Altura: "+str(self.altura))
    
def arrancar():
    nuevaPersona = DatosPersonales ("Carlota Manrique",34,'O',170)
    nuevaPersona.info()

if __name__ == '__main__':
    arrancar()