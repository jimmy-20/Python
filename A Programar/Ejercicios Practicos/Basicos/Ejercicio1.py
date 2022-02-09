#1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio).

def MaximoNumeros(a,b):
    if a>b:
        return a
    else:
        return b

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese el siguiente numero: "))

print(f"El mayor de los numeros es {MaximoNumeros(num1,num2)}")

