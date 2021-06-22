def suma (a,b):
    return a+b

def resta(a,b):
    return a-b

def producto(a,b):
    return a*b

def tablas_multi(producto):
    cantidad = int(input("Ingrese la cantidad de veces a multiplicar: "))
    for i in range(0,cantidad):
        resultado = i*producto
        print(str(producto)+" X "+str(i)+" = "+str(resultado))    

def calculadora():

    opcion = int(input("Ingrese una opción: "))

    if(opcion == 1):
        opc_a = int(input("Ingrese el valor de a: "))
        opc_b = int(input("Ingrese el valor de b: "))
        resultado = suma(opc_a,opc_b)

        print("El resultado de la suma es: "+str(resultado))
    elif (opcion == 2):
        opc_a = int(input("Ingrese el valor de a: "))
        opc_b = int(input("Ingrese el valor de b: "))
        resultado = resta(opc_a,opc_b)

        print("El resultado de la resta es: "+str(resultado))
    elif (opcion == 3):
        opc_a = int(input("Ingrese el valor de a: "))
        opc_b = int(input("Ingrese el valor de b: "))
        resultado = producto(opc_a,opc_b)

        print("El resultado del producto es igual a: "+str(resultado))
    elif (opcion==4):
        valor = int(input("Ingrese el producto: "))
        resultado = tablas_multi(valor)
        
if __name__ == '__main__':
    calculadora()