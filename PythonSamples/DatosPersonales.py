class DatosPersonales:
    
    def __init__(self, name, surname, age, height,country):
        self._name    = name
        self._surname = surname
        self._age     = age
        self._height  = height
        self._country = country

    ##Getters    
    @property
    def name(self):
        return  self._name 
    def surname(self):
	    return  self._surname     
    def age(self):
	    return self._age     
    def height(self):
	    return self._height
    def country(self):
        return self._country
     
    @name.setter
    def name(self,name):
        self._name = name
    def surname(self, surname):
	    self._surname = surname
    def age (self,age):
	    self._age = age
    def country(self, country):
        self._country = country

class Mecanico(DatosPersonales):
    def __init__(self, name, surname, age, height, country,labour_age,college):
        super().__init__(name, surname, age, height, country)
        self._labour_age = labour_age
        self._college = college
    
def run():

    mecanico1 = Mecanico("Juan","Pérez",50,165,"España",25,"INE")

    mecanico1.name = input("Ingrese el nombre: ")
    mecanico1.surname = input("Ingrese los apellidos: ")
    mecanico1.age = int(input("Ingrese la edad: "))
    mecanico1.height = int(input("Ingrese la altura: "))
    mecanico1.country = input("Ingrese el país: ")
    mecanico1.labour_age = int(input("¿Cuántos años laboró como mecánico: ?"))
    mecanico1.college = input("Ingrese la escuela en dónde fue egresado: ")

    print()
    print("Nombre: "+mecanico1.name)
    print("Apellidos: "+mecanico1.surname)
    print("Edad: "+str(mecanico1.age))
    print("País: "+mecanico1.country)
    print("Años laborando: "+str(mecanico1.labour_age))
    print("Escuela: "+mecanico1.escuela)

    #persona1 = DatosPersonales("Dewin","Acosta",28,170,"Colombia")

    #persona1.name = input("Ingrese tu nombre: ")
    #persona1.surname = input("Ingrese tus apellidos: ")
    #persona1.age = int(input("Ingrese tu edad: "))
    #persona1.height = int(input("Ingrese tu estatura: "))

    #if persona1.age>18:
    #    print("Nombre: "+persona1.name)
    #    print("Apellidos: "+persona1.surname)
    #    print("Edad: "+str(persona1.age))
    #    print("Altura: "+str(persona1.height))
    #    print("Esta persona es mayor de edad")
    #elif persona1.age<18:
    #    print("Nombre: "+persona1.name)
    #    print("Apellidos: "+persona1.surname)
    #    print("Edad: "+str(persona1.age))
    #    print("Altura: "+str(persona1.height))      

if __name__ == '__main__':
    run()
    
    