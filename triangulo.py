def triangulo():
	cantidad = int(input("Ingrese la cantidad de lineas: "))
	
	for i in range(1,cantidad):
		for j in range (0,i):
			print("x",end="")
		print("\n")


if __name__ == '__main__':
	triangulo()
