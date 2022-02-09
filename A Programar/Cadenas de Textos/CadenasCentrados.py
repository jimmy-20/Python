texto = "Esto es un texto para el ejemplo"

#Empieza y termina con
print("Si la cadena empieza con: ",texto.startswith("Esto"))
print("Si la cadena termina en: ",texto.endswith("Realizar"))

#Alinear textos
print(texto.center(34,'+'))

longitud = len(texto)
print(longitud)

#Añadir caracteres por la izquierda o derecha
print(texto.ljust(35,'-'))
print(texto.rjust(35,'+'))

#Eliminar parte de la cadena
textSpace = "    Esto es   una cadena con    espacios y /*-$   "
print(textSpace.strip())

#Sustituir caracteres
print(textSpace.replace("-","Hola"))