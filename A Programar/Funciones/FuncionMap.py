lista = [1,2,3,4,5,6,7,8,9]

#     List( map ((lambda var: NuevoValor), Array/Lista))
print(list(map((lambda valor: valor*valor), lista)))
print(lista)

#map( (Funcion Lambda), Array/Lista)
#list(map)

#Funcion Filter
print(list(filter((lambda valor: valor % 2 == 0),lista)))

#Funcion Reduce
from ast import Lambda
import functools
print(str(functools.reduce((lambda x,resultado : x+resultado),lista)))