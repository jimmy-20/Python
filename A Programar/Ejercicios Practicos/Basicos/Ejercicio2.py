#2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def Maximo(a,b,c):
    if ( (a>b) & (a>c)):
        return a
    elif ((b>a) & (b>c)):
        return b
    elif ((c>a) & (c>b)):
        return c
    else:
        return "Son iguales"       

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

print(type(Maximo(num1,num2,num3)))
print("El mayor numero es: ",Maximo(num1,num2,num3))