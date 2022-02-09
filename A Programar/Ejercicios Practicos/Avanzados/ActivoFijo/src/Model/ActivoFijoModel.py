class ActivosModel():
    activosFijos = []

    def __init__(self):
        self.activosFijos = []

    def Agregar(self,af):
        self.activosFijos.append(af)

    def VerTodos(self):
        return self.activosFijos

    def Actualizar(self,af,index):
        self.activosFijos.pop(index)
        self.activosFijos.insert(index,af)

    def Eliminar(self,id):
        index = self.Buscar(id)

        if str(index).isdigit():
            self.activosFijos.pop(index)
            return f"Se elimino el ActivoFijo con id {id}"
        else:
            return "Id no encontrado"

    def Buscar(self,id):
        index = 0
        for af in self.activosFijos:
            if id == af.GetId():
                return index
            index +=1
        return "NONE"
