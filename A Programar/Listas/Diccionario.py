diccionario = {'Nombre' : 'Jose', 'Apellidos' : 'Ojeada' , 
              'Tutoriales' : ["Python","JavaScript","PHP"]}
print(type(diccionario))
print(diccionario)

print()

#Mostrar valor por medio de una clave
print(diccionario['Nombre'])
print(diccionario['Tutoriales'])

print(diccionario['Tutoriales'][1]) 
print()

#Recorrer un diccionario
for clave in diccionario:
    print(clave, ":", diccionario[clave])
print()
#Metodos de los diccionarios
persona = dict(nombre = "Jose",apellidos = "Ojeda", edad = 48)

print(type(persona))
print(persona)

diccionario02 = dict(zip('aeiou',[1,2,3,4,5]))
print(diccionario02)

print(diccionario02.items())
print(diccionario02.keys())

print(diccionario02.values())

#diccionario02.clear()
print(diccionario02)

copiaDiccionario = diccionario02.copy()
print(copiaDiccionario)

diccionario03 = dict.fromkeys(['a','e','i','o','u'],34)
print(diccionario03)

print(diccionario.get('Nombre'))
print(diccionario.get('Nombr'))

print()
borrado = diccionario.pop('Nombre')
print(borrado)
print(diccionario)

print()
#Actualizar un diccionario
diccionario02 = {'Provincia' : 'Sevilla','Nombre' : 'Josue'}
print(diccionario)
diccionario.update(diccionario02)
print(diccionario)