#Guardar y abrir datos en un archivo
escritura = open("Archivo.txt","w")
escritura.write("Esto se escribe en el archivo \ny esto en la linea siguiente")

escritura.close()
lectura = open("Archivo.txt","r")

LeeLinea = lectura.readline()
print(LeeLinea)

leeTodo = lectura.read()
lectura.close()

print(leeTodo)