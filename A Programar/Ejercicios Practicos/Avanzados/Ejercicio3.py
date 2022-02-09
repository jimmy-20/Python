#3) Este programa muestra primero el listado de categorías 
#de películas y pide al usuario que introduzca el código 
#de la categoría de la película y posterior a ello pide 
#que el usuario introduzca el número de días de atraso, 
# y así se muestra al final el total a pagar.

def Header():
    print("Id           Categorias          Precio          Retraso / dias")

def Body():
    print("1            Favoritos           $2.50           $0.50")
    print("2            Nuevos              $3.00           $0.75")
    print("3            Estrenos            $3.50           $1.00")
    print("4            SuperEstrenos       $4.00           $1.50")

def CalculoPago(id,atraso):
    if (id == 1):
        return 2.50 + (0.50 * atraso)
    elif id == 2:
        return 3 + (0.75 * atraso)
    elif id == 3:
        return 3.50 + (1 * atraso)
    elif id == 4:
        return 4 + (1.50 * atraso)
    else:
        return False



flag = True

while (flag):
    Header()
    Body()

    id = int(input("\nIntroduzca el codigo de la categoria: "))
    atraso = int(input("Numeros dias de atraso: "))

    if (CalculoPago(id,atraso) == False):
        print("Categoria de Pelicula no existe, ingrese de nuevo")
    else:
        print("El total a pagar es de: ",CalculoPago(id,atraso))

    print("\nDesea salir?")
    print("1.Si")
    print("2.No")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        break
    else:
        continue

print("Gracias por su compra!")