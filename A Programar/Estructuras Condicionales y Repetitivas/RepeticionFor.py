#Tabla de multiplicar con For
tabla = int(input("Que tabla desea ver?: "))

print(f"Tabla del {tabla}")

#Repetir mientras sea menor que 11

for contador in range (1,11):
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")

#Ejemplo con lista
nombres = ["Jose","Maria","Lucia","Leonor"]

for nombre in nombres:
    print(nombre)