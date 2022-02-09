print("Bienvenido al primer programa de Python")
print("Datos basicos")
print("Tipo Entero: ", type(1))
print("Tipo Float: ", type(1.1))
print("Tipo String: ", type(str("Hola")))
print("Tipo Boolean: ", type(True))

print()

print("Datos avanzados")
print("Tipo Lista: ", type([1, 2, 3]))
print("Tipo Diccionario: ", type({1: "uno", 2: "dos"}))
print("Tipo Set: ", type({1, 2, 3}))
print("Tipo None: ", type(None))
print("Tipo Todo: ", type(type(None)))
print("Tipo Object: ", type(object))
print("Tipo Function: ", type(print))

print("Ejemplos con cadenas")
print("Hola, " + " mundo")
print ("Saludos","mundo")
print("Saludo " *4)

variable = "Cadena en variable"
variable = "Suma esto a " + variable
print (variable)
print(variable[3])
print(variable[+1])
print(variable[0:9])
print(len(variable))
print(variable.upper())
print(variable.lower())
print(variable.capitalize())

print()

cadena = "    Esto   es    una    cadena   con    muchos   espacios"
print(cadena.strip())
cadena = "Hola esto es un texto sin reemplazar"
print(cadena)
print(cadena.replace("sin reemplazar" , "con reemplazo"))
