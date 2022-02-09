#De la galería de productos, el usuario introducirá el código 
# y el número de unidades del producto que desea comprar. 
# El programa determinará el total a pagar, como una factura.
#Una variante a este ejercicio que lo haría un 
#poco más complejo sería dar la posibilidad de seguir 
#ingresando diferentes códigos de productos con 
#sus respectivas cantidades, y cuando el usuario 
#desee terminar el cálculo de la factura completa con todas sus compras



def Products_Cathegory():
    print("ID       NOMBRE                TIPO           PRECIO")
    print("1        COCACOLA 2L           Bebidas        C$35")
    print("2        CENTAVITOS GRANDE     Snacks         C$28")
    print("3        BONOBON CHOCOLATE     Dulce          C$7")
    print("4        HELADO ESKIMO FRESA   Refrigerante   C$20")

def Header():
    print("         SUPERMERCADO SOZA S.A           ")
    print("         Praderas de Sandino H-9         ")


flagCompra = True
flagFactura = True

while flagCompra:

    Header()
    while flagFactura:

        Products_Cathegory()
        IdProduct = int(input("Ingrese el codigo del producto:"))
        Quantity = int(input("Cantidad a llevar: "))
        if IdProduct == 1:
            print("COCACOLA 2L")
            print("C$35")
            print("Total a pagar:", Quantity * 35)
        elif IdProduct == 2:
            print("CENTAVITOS GRANDE")
            print("C$28")
            print("Total a pagar:", Quantity * 28)
        elif IdProduct == 3:
            print("BONOBON CHOCOLATE")
            print("C$7")
            print("Total a pagar:", Quantity * 7)
        elif IdProduct == 4:
            print("HELADO ESKIMO FRESA")
            print("C$20")
            print("Total a pagar:", Quantity * 20)
        else:
            print("Codigo invalido")
        print("Desea continuar comprando?")
        print("1. Si")
        print("2. No")
        flagFactura = int(input("Ingrese una opcion: "))
        if flagFactura == 1:
            flagFactura = True
        else:
            flagFactura = False
            flagCompra = False
            print("Gracias por su compra")
            print("Vuelva pronto")
            break
        