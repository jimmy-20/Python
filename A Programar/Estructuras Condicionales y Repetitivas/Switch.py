#Usuario nos da el numero del mes y devuelve el nombre del mes

def DameMes(mes):

    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Dicimebre"
    }

    return switcher.get(mes, "Invalid month")

mes = int(input("Introduce el numero del mes: "))
print(DameMes(mes))