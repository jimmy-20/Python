def Calcular(num1,num2,operacion):
    def Sumar(num1,num2):
        return num1+num2

    def Restar(num1,num2):
        return num1-num2

    def Multiplicar(num1,num2):
        return num1*num2

    def Dividir(num1,num2):
        return num1/num2
    
    Resultado = 0
    Operador = ""

    if operacion == "Suma":
        Resultado = Sumar(num1,num2)
        Operador = "+"

    elif operacion == "Resta":
        Resultado = Restar(num1,num2)
        Operador = "-"
    elif operacion == "Multiplicacion":
        Resultado = Multiplicar(num1,num2)
        Operador = "x"
    else:
        Resultado = Dividir(num1,num2)
        Operador = "/"

    print(f"{num1}  {Operador}  {num2} = {Resultado}")



num1 = int(input("Primer Numero: "))
num2 = int(input("Segundo Numero: "))
Calcular(num1,num2,"Multiplicacion")