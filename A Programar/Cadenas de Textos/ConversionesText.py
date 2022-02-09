#Convertir a Minusculas
cad = "EjemPlo de CadENa de Texto"
cad.lower()

print(cad.lower())

#Convertir a Mayusculas
print(cad.upper())

#Convertir la primera letra en Mayus
print(cad.capitalize())

#Primera letra de cada palabra en Mayuscula
print(cad.title())

#Invertir minusculas a Mayusculas y Viceversa
print(cad.swapcase())

#Verifica si la cadena esta en Mayuscula
print(cad.isupper())

cad2 = "MAYUSCULAS"
print(cad2.isupper())

#Verifica si la cadena esta en minuscylas
print(cad2.islower())

#Verifica si la cadena es numerica
print(cad2.isnumeric())

numeros = "1234"
print(numeros.isnumeric())

#Si la cadena es Alfa-Numercia
print(cad2.isalnum())

#Verifica si es un titulo
print(cad.istitle())

titulo = "Hola Mundo"
print(titulo.istitle())