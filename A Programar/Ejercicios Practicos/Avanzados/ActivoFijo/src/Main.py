from Pojo.ActivoFijo import ActivoFijo
from Model.ActivoFijoModel import ActivosModel
from Model.Depreciacion import MetodoDepreciacion

def Menu():
    print("1. Nuevo activo fijo")
    print("2. Visualizar todos")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Depreciacion")
    print("6. Salir")

def Header():
    print("{:5}{:20}{:20}{:20}".format("Id","Nombre","Tipo","Valor"))
    print("---------------------------------------------------------")

def Body(activos):
    for af in (activos):
        print("{:5}{:20}{:20}{:20}".format(str(af.GetId()),str(af.GetNombre()),str(af.GetTipo()),str(af.GetValor())))

def getActivoFijo(activos,id):
    index = 0
    for af in activos:
        print(f"Id entrante {id}, id del AF {af.GetId()}")
        if id == af.GetId():
            return id,index
        index +=1
    return "NONE","NONE"

Id = 0
activosFijos = ActivosModel()

flag =True
while(flag):
    print() #Espacio de linea
    Menu()
    opcion = int(input("Selecciona una opcion >> "))
    print()
    if opcion ==1:
        print("----- NUEVO ACTIVOFIJO -----")
        Id +=1
        Nombre =input("Nombre: ")
        Tipo = input("Tipo de Activo: ")
        Valor = float(input("Valor del Activo: "))

        af = ActivoFijo(Id,Nombre,Tipo,Valor)
        activosFijos.Agregar(af)
    elif opcion == 2:
        Header()
        Body(activosFijos.VerTodos())
    elif opcion == 3:
        Header()
        Body(activosFijos.VerTodos())
        idBuscar = int(input("\nIngrese el Id para actualizar:"))

        index = activosFijos.Buscar(idBuscar)
        if str(index).isdigit() == True:
            Nombre =input("Nombre: ")
            Tipo = input("Tipo de Activo: ")
            Valor = float(input("Valor del Activo: "))

            af = ActivoFijo(idBuscar,Nombre,Tipo,Valor)
            activosFijos.Actualizar(af,index)
        else:
            print("No existe el Id Ingresado")

    elif opcion == 4:
        Header()
        Body(activosFijos.VerTodos())
        index = int(input("Ingrese el Id a eliminar: "))

        print(activosFijos.Eliminar(index)) #Regresa un mensaje de confirmacion

    elif opcion == 5:
        MetodoDepreciacion.LineaRecta(activosFijos.VerTodos())
    elif opcion == 6:
        flag = False
    else:
        print("Opcion invalida")
