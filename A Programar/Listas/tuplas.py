colores = ("Verde","Amarillo","Rojo","Azul")
print(type(colores))
print(colores)

print(colores[:2])

tupla = ()
print(tupla)

#print(colores[4]) Excepcion de indice inexistente
#colores[2] = "Rosa" Excepcion de error de asignacion

print(len(colores))
tuplaUnitaria = (50,)

print(type(tuplaUnitaria))
print(len(tuplaUnitaria))

#Empaquetado de tuplas
a,b,c = 10,"Jose",22.34
tupla = a,b,c

print(tupla)

#Desempaquetado de tuplas
d,e,f = tupla
print(d,e,f)