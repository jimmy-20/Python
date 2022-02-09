#4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def SiVocal(letra):
    letra = str.lower(letra)
    if str.isalpha:
        if ( (letra == "a") | (letra == "e") | (letra == "i") | (letra == "o") | (letra == "u")):
            return True
    return False

print(SiVocal("b"))