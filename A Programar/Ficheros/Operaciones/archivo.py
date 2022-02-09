import os

carpeta = "C:\\Users\Pc\Desktop\JASO\Sintaxis de Programacion\Python\A Programar\Ficheros\Operaciones"
print(carpeta)

listado = os.listdir(carpeta)
print(listado)
print(type(listado))

#Filtrado
for archivo in listado:
    if (archivo.endswith(".py")):
        print("Fichero Py encontrado")
        print(f"{archivo}")
    else:
        print("Sin resultados")

print()
#Otra forma de filtrar
filtrado = [archivo for archivo in listado if archivo.endswith(".py")]
print("Se encontro los siguientes archivos:")
print(filtrado)

#Cambio de Directorio
os.chdir("C:\\Users\Pc\Desktop\JASO\Sintaxis de Programacion\Python\A Programar\Ficheros\Operaciones")

#Renombrar
os.rename("Activofijo.txt","ActivoFijo.txt")

#Borrar un archivo
Fichero = open("Prueba.txt","w")
Fichero.write("Hola mundo en un fichero")
Fichero.close()

os.remove("Prueba.txt")
print("Se borro el archivo Prueba.txt")