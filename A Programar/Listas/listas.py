lista = [1,2,3,"Jose",[7,8],12]

print(type(lista))
print(lista)

print(lista[2:4:2])

print("Imprimiendo una lista con un bucle For")
for element in lista:
    print(element)

print("")

lista.append(10)
lista.append("Jaso")
lista.append([13,14,15])
print(lista)

lista.extend([16,17,18])
print(lista)
lista.remove('Jose')
print(lista)

print(lista.index([7,8]))
print(lista.count(2))

lista.reverse()
print(lista)