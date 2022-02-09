#8 - Definir una función superposicion() que tome dos listas 
# y devuelva True si tienen al menos 1 miembro en común o 
# devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def Superposicion(lista1,lista2):
    for chara1 in (lista1):
        for chara2 in (lista2):
            if (chara1 == chara2):
                return True
    return False

numeros = {1,2,3,4,5}
vocales = {"a","e","i","o","u"}

alphaNum = {1,2,3,"o","u"}

print(Superposicion(numeros,alphaNum))