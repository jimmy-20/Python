#9 - Definir una función generar_n_caracteres() que tome un entero n 
# y devuelva el caracter multiplicado por n. 
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def Generar_n_caracteres(n,chara):
    if (not str.isdigit(str(n)) ):
        return "El primer parametro debe ser un numero"

    return chara * n

veces = 2
chara = "x"
print(Generar_n_caracteres(veces,chara))