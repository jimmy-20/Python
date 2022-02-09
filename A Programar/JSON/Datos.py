import json
from urllib import request

url = "https://my.api.mockaroo.com/personas_demo.json?key=52756c70"
respuesta = request.urlopen(url)
#print(respuesta)

contenido = respuesta.read()
#print(contenido)

json_obtenido = json.loads(contenido.decode('utf-8'))
print(json_obtenido)

for persona in json_obtenido:
    print(f"Nombre: {persona['Nombres']}")
    print(f"Apellidos: {persona['Apellidos']}")
    print(f"Correo: {persona['Correo']}")
    print(f"Genero: {persona['Genero']}")
    print("*************************\n")