def sumatoria():
	suma_inicio = 0
	suma_acumulada = 0
	
	while(suma_inicio>=0):
		suma_inicio = int(input("Ingrese un numero que no sea negativo: "))
		suma_acumulada = suma_acumulada+suma_inicio
	
	print("Sumatoria de numeros: "+str(suma_acumulada))


if __name__ == '__main__':
	sumatoria()
