import os

num1 = 45
num2 = 0
try:
    resultado = num1/num2

    print(resultado)
except:
    print("Division por cero imposible")
finally:
    print("Esto se ejecuta siempre")

try:
    os.remove(os.getcwd() + "/arch454.txt")
except:
    print("Archino no existe en el directorio actual")
finally:
    print("Fin de la ejecucion")