num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: 3"))

if (num1 > num2):
    print(f"El numero {num1} es mayor que {num2}")
elif(num1 < num2):
    print(f"El numero {num1} es menor que {num2}")
else:
    print("Los numeros son iguales")

print("Hemos terminado de comparar")

#Segundo ejemplo
edad = int(input("Dime tu edad y te indico tu tarifa: "))

if edad < 5:
    precio = 0
elif edad < 15:
    precio = 5
elif edad < 65:
    precio = 20
else:
    precio = 15

print(f"Tu tarifa para entrar es de {precio}")