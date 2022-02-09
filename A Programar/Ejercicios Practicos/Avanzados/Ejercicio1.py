#1) Este programa pide primeramente la cantidad total 
# de compras de una persona. Si la cantidad es inferior 
# a $100.00, el programa dirá que el cliente no aplica
# a la promoción. Pero si la persona ingresa una cantidad 
# en compras igual o superior a $100.00, el programa genera 
# de forma aleatoria un número entero del cero al cinco. 
# Cada número corresponderá a un color diferente de cinco colores 
# de bolas que hay para determinar el descuento que el 
# cliente recibirá como premio. Si la bola aleatoria es 
# color blanco, no hay descuento, 
# pero si es uno de los otros cuatro colores, 
# sí se aplicará un descuento determinado según la tabla que  
# aparecerá, y ese descuento se aplicará sobre el 
# total de compra que introdujo inicialmente el usuario, 
# de manera que el programa mostrará un nuevo valor a pagar 
# luego de haber aplicado el descuento.

compra_Total = float(input("Ingrese la cantidad total de compras: "))

if compra_Total < 100:
    print("El cliente no aplica a la promoción")
else:
    import random
    bola = random.randint(0,5)
    if bola == 0:
        print("El cliente no aplica a la promoción")
    else:
        if bola == 1:
            print("El cliente aplica a la promoción y recibe un descuento del 10%")
            print("El cliente debe pagar: ", compra_Total * 0.9)
        elif bola == 2:
            print("El cliente aplica a la promoción y recibe un descuento del 20%")
            print("El cliente debe pagar: ", compra_Total * 0.8)
        elif bola == 3:
            print("El cliente aplica a la promoción y recibe un descuento del 30%")
            print("El cliente debe pagar: ", compra_Total * 0.7)
        elif bola == 4:
            print("El cliente aplica a la promoción y recibe un descuento del 40%")
            print("El cliente debe pagar: ", compra_Total * 0.6)
        elif bola == 5:
            print("El cliente aplica a la promoción y recibe un descuento del 50%")
            print("El cliente debe pagar: ", compra_Total * 0.5)