def Suma(a,b):
    return a+b

def Resta(a,b):
    return a-b

def Multiplicacion(a,b):
    return a*b

def Division(a,b):
    if b == 0:
        return "INDEFINIDO"

    return a/b


print ("Calculadora basica")

opcion = 1

while(opcion != 0):
    print("\n1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")
    print()

    opcion = int(input("Que desea hacer?: "))

    if opcion == 0:
        break
    
    while (opcion < 0) | (opcion > 4):
        opcion = int(input("Ingrese una opción valida: "))
    
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    if opcion == 1:
        print(f"La suma es: { Suma(num1,num2) }")
    elif opcion == 2:
        print(f"La resta es: {Resta(num1,num2)}")
    elif opcion == 3:
        print (f"La multiplicación es: {Multiplicacion(num1,num2)}")
    else:
        print(f"La división es: {Division(num1,num2)}")
    
print("Adios")

