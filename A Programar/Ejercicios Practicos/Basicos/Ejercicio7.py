#7 - Definir una función es_palindromo() que reconoce palíndromos 
# (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo ("radar") tendría que devolver True.

def inversa(cadena):
    invertida = ""
    contador = len(cadena)
    while contador > 0:
        invertida += cadena[contador-1]
        contador -=1
    return invertida

def Es_Palindromo(cadena):
    Invertida = inversa(cadena)
    tamanio = len(cadena)

    for index in range(1,tamanio):
        if cadena[index] != Invertida[index]:
            return False
    
    return True


Cadena = "radar"
if (Es_Palindromo(Cadena) == True):
    print("Es palindromo la palabra",Cadena)
else:
    print("No es Palindromo")