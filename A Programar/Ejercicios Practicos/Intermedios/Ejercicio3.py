#Has un programa que pida al usuario una cantidad de dolares, 
# una tasa de interés y un numero de años. 
# Muestra por pantalla en cuanto se habrá convertido el 
# capital inicial transcurridos esos años si cada año se 
# aplica la tasa de interés introducida.
#Recordar que un capital C dolares a un interés del x por cien 
# durante n años se convierte en 
# C * (1 + x/100)elevado a n (años). 
# Probar el programa sabiendo que una cantidad de 10000 
# dolares al 4.5% de interés anual se convierte en 24117.14 
# dolares al cabo de 20 años.

def Capital(capital, interes, años):
    capital = capital * (1 + interes/100)**años
    print("El capital al cabo de {} años es de {}".format(años, round(capital)))

capital = float(input("Introduce el capital: "))
interes = float(input("Introduce la tasa de interés: "))
años = int(input("Introduce el numero de años: "))
Capital(capital, interes, años)


