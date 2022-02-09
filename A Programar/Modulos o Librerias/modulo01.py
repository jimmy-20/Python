import math

#from math import sqrt

numero = int(input("Dime un numero: "))
print(str(math.sqrt(numero)))

#Imprimir numero al azar
from random import randint as azar
#from random import *

continua = "s"
while ((continua == "s") or (continua == "S")):
    print()
    lanzarDado = azar(1,6)
    print("Has sacado un ",lanzarDado)
    continua = input("Desea continuar? S/N: ")