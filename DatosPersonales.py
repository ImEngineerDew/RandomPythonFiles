class DatosPersonales:
    
    def __init__(self,name,surname,age,height):
        self._name    = name
        self._surname = surname
        self._age     = age
        self._height  = age
    
    ##Getters
    @property
    def name(self):
        return self._name
    def surname(self):
        return self._surname
    def age(self):
        return self._age
    def height(self):
        return self._height

    ##Setters
    @name.setter 
    def name(self,name):
        self._name = name

        

if __name__ == '__main__':
    persona = DatosPersonales("Dewin","Acosta",28,170)
    persona.name = input("Ingrese el nombe de la persona: ")
    persona.surname = input("Ingrese los apellidos: ")
    print("Nombre: "+persona.name)
    print("Apellidos: "+persona.surname)



