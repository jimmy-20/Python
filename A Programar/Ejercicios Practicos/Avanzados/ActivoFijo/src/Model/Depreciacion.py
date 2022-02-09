class MetodoDepreciacion():
    #Edificios: 10 - 30 años
    #Equipos de transporte: 3 - 8 años
    #Maquinaria y equipos: 5 - 10 años
    #Bienes muebles: 2 - 10 años


    def Header(activofijos,años = 0):

        for af in activofijos:
            tipo = MetodoDepreciacion.SwitchTipo(af.GetTipo())
            if años < tipo:
                años = tipo

        print("{:20}".format("Activo"),end = " ")
        for i in range(1,años+1):
            print("{:10}".format(str(i)),end = " ")

        print("\n----------------------------------------------------")

    def Body(depreciacion,años):
        total = 0
        for i in range (0,años):
            print("{:10}".format(str(depreciacion)),end = " ")
            total += depreciacion

        print("{:8}".format(str(round(total,2))))

    #Regresa la cantidad de Años en dependecia del tipo de activo
    def SwitchTipo(tipoActivo):
        despreciables = {"Edificios":10, "Vehiculo": 3, "Maquinaria": 5,"Bienes": 2}
        return despreciables.get(tipoActivo,0)

    def LineaRecta(activosFijos):
        #Regresa la depreciacion del activo
        def Calculo(af):
            años = MetodoDepreciacion.SwitchTipo(af.GetTipo())
            return round(af.GetValor()/años,2),años

        MetodoDepreciacion.Header(activosFijos)
        #Imprime la depreciacion de cada activo
        for af in activosFijos:
            depreciacion,años = Calculo(af)
            print("{:20}".format(af.GetNombre()),end = " ")
            MetodoDepreciacion.Body(depreciacion,años) #Imprime la cantidad de depreciaciones
        print() #Salto de linea
