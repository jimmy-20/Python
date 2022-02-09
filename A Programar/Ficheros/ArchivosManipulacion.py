import os

#Crear carpeta o directorio
os.makedirs("MiCarpeta")

#Listar el contenido del directorio
print(os.listdir("./"))

#Mostrar Directorio actual
print(os.getcwd())

#Mostrar Size de una carpeta
print(os.path.getsize("MiCarpeta"))

#Comprobar si es un archivo 
print (os.path.isfile("MiCarpeta"))

#Comprobar si es directorio
print(os.path.isdir("MiCarpeta"))

#Cambiar de directorio
os.chdir("MiCarpeta")

#Directorio actual
os.chdir("../")
print(os.getcwd())

#Renombrar la carpeta
os.rename("MiCarpeta","Mi_Carpeta")

#Borrar un archivo
os.remove(os.getcwd()+"/Archivo.txt")

print(os.listdir("./"))

#Borrar una carpeta
os.rmdir("Mi_Carpeta")

os.chdir("../")
print(os.listdir("./"))