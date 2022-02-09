#Tabla de multiplicar
tabla = int(input("Que tabla quieres calcular?: "))

#Creamos variable contador
contador = 1
print(f"\nTabla del {tabla}")

#Repeticion
while contador < 11 :
    resultado = tabla * contador

    print(f"{tabla} x {contador} = {resultado}")
    contador = contador + 1

    if contador == 4:
        print("El contador es igual a 4 y no continuo")
        break

print("\nFin de la tabla")