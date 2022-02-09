frutas = ["Manzana","Pera","Uvas"]
print(type(frutas))

cantidadManzana = 5
precioManzana = 20
total = cantidadManzana * precioManzana

pedido1 = [cantidadManzana,precioManzana,total]
pedido2 = [3,22.5,3*22.5]
pedido3 = [4,17,4*17]

pedidos = [pedido1,pedido2,pedido3]
print(pedidos)

#Lista vacia
#ListaVacia = []

frutas.append("Banano")
frutas.insert(2,"Sandia")
print(frutas)

frutas.pop()
print(frutas)

#Longitud de la lista
print(len(frutas))

#Esta en la lista?
print("Pera" in frutas)



#Ejemplo agregar con bucle
cuadrados = []
for numero in range(1,10):
    cuadrados.append(numero**2)
print(cuadrados)

print(f"El minimo y maximo son: {min(cuadrados)} y {max(cuadrados)}")
print("La suma de los cuadrados es",sum(cuadrados))