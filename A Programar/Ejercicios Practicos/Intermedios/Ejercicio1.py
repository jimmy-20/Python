#Escribe un programa que te permita jugar a una versión simplificada del
#juego Master Mind. El juego consistirá en adivinar una cadena de números
#distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
#a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
#cadena de números. En cada intento, el programa informará de cuántos números
#han sido acertados (el programa considerará que se ha acertado un número si
#coincide el valor y la posición).
import random


def EsIgual(cadena,numero):
    if (cadena == str(numero)):
        return True
    return False

def Pista(cadena,numero):
    contador = 0
    for chara in cadena:
        for chara2 in str(numero):
            if (chara == chara2):
                contador+=1
    return contador

longitud = int(input("Dime la longitud de la cadena: "))
cadena = ""
numero = 0
for i in range(0,longitud):
    cadena = cadena + str(random.randint(0,9))

while(EsIgual(cadena,numero) == False):
    numero = int(input("Intenta adivinar el numero: "))
    print(f"Has adivinado {Pista(cadena,numero)} digitos")

print("\n Has acertado!!!")
