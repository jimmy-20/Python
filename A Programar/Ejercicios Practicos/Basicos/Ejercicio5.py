#5 - Escribir una función sum() y una función multip() que sumen 
# y multipliquen respectivamente todos los números de una lista. 
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def Suma(lista):
    resultado = 0
    for num in lista:
        resultado =+ num
    return resultado

def Multiplicar(lista):
    Producto = 1
    for num in lista:
        Producto = Producto * num
    return Producto

Array = {1,2,3,4}
print("La Suma es: ",Suma(Array))
print("La Multiplicacion es: ",Multiplicar(Array))