#6 - Definir una función inversa() que calcule la inversión de una cadena. 
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    invertida = ""
    contador = len(cadena)
    while contador > 0:
        invertida += cadena[contador-1]
        contador -=1
    return invertida

print(inversa("Estoy Probando"))
