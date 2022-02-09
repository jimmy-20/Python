class Vehiculo:
    def __init__(self,color,velocidadMax,marca):
        self.color = color
        self.velocidad = 0
        self.velocidadMax = velocidadMax
        self.marca = marca

    def Arrancar(self):
        print("Arrancado",self.marca)

    def Acelerar(self):
        if self.velocidad == 0 :
            self.velocidad = 10
        else:
            self.velocidad = self.velocidad + 10
        print("Velocidad = ",self.velocidad)

    def Frenar(self):
        if self.velocidad > 10:
            self.velocidad = self.velocidad - 10
        else:
            self.velocidad = 0
    
    def Estado (self):
        print(f"Soy de la marca {self.marca}, color {self.color} y velocidad maxima {self.velocidadMax}")

Toyota = Vehiculo("Rojo",120,"Toyota")
Yaris = Vehiculo("Verde",130,"Yaris")

Toyota.Arrancar()
Toyota.Acelerar()

Yaris.Arrancar()
Yaris.Acelerar()

Toyota.Acelerar()
Toyota.Estado()

Yaris.Frenar()
Yaris.Estado()