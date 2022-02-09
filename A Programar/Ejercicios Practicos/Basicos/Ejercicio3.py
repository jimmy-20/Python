#3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que python tiene la función len() incorporada, 
# pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def SizeList(lista):
    contador = 0
    for element in lista:
        contador += 1
    return contador

Numeros = {10,5,2,6,7,8}
Vocales = {'a','e','i','o','u'}

print(SizeList(Numeros))
print(SizeList(Vocales))