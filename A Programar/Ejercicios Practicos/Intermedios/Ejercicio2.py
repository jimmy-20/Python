#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
#las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
#últimas tiene que decir que riman un poco y si no, que no riman.

def Similares(palabra1, palabra2):
    if palabra1[-3] == palabra2[-3:]:
        print("Las dos palabras son similares")
    elif palabra1[-2:] == palabra2[-2:]:
        print("Las dos palabras son similares un poco")
    else:
        print("Las dos palabras no son similares")

cadena1 = input("Introduce una palabra: ")
cadena2 = input("Introduce otra palabra: ")
Similares(cadena1, cadena2)
