class ActivoFijo():
    def __init__(self,Id,Nombre, Tipo,Valor):
        self.Id = Id
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Valor = Valor
        print("Se ha creado el ActivoFijo")

    def GetId(self):
        return self.Id

    def GetNombre(self):
        return self.Nombre

    def GetTipo(self):
        return self.Tipo

    def GetValor(self):
        return self.Valor

    def SetNombre(self,Nombre):
        self.Nombre = Nombre

    def SetTipo(self,Tipo):
        self.Tipo = Tipo

    def SetValor(self,Valor):
        self.Valor = Valor
