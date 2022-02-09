#10 - Definir un histograma procedimiento() que tome una lista
# de números enteros e imprima un histograma en la pantalla. 
# Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

def Procedimiento(lista):
    histograma = ""
    for num in lista:
        histograma = histograma + ("*" * num) + "\n"
    
    return histograma

def Procedimiento2(lista):
    for num in lista:
        print(num * "*")

lista = {1,3,2}

print(Procedimiento(lista))

print()

Procedimiento2(lista)
