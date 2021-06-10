def nombres():
	
	nombre = 0	
	nombre = input("Ingrese un nombre que tenga como mínimo 6 letras y máximo 12 letras: ")
	acumulador = len(nombre)
	
	if(acumulador<6):
		print(nombre)
		print("El nombre contiene menos de seis caracteres")
		nombre = input("Ingrese un nombre que tenga como mínimo 6 letras y máximo 12 letras: ")
	elif(acumulador>12):
		print(nombre)
		print("El nombre contiene más de seis caracteres")
		nombre = input("Ingrese un nombre que tenga como mínimo 6 letras y máximo 12 letras: ")
	else:
		print("NOMBRE DE USUARIO VÁLIDO")

	
if __name__ == '__main__':
	nombres()
